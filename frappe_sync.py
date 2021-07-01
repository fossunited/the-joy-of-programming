import os
import click
from frappeclient import FrappeClient
from pathlib import Path
import yaml

COURSE_NAME = "the-joy-of-programming"

API_KEY = os.getenv("FRAPPE_API_KEY")
API_SECRET = os.getenv("FRAPPE_API_SECRET")

class Document:
    DOCTYPE = None
    FIELDS = []

    def push(self):
        doc = {k: self.data[k] for k in self.FIELDS}
        print(f"updaing {self.name} ...")

        data = {
            "doctype": self.DOCTYPE,
            "name": self.name,
            "doc": doc
        }
        return invoke_method(self.frappe, "mon_school.api.save_document", data=data)

def invoke_method(frappe, method, data):
    url = frappe.url + "/api/method/" + method
    result = frappe.session.post(url, json=data).json()
    print(result)
    message = result['message']
    if message.get("ok"):
        return message
    else:
        raise Exception(message.get("error") or f"unknown error: {message}")

class Course:
    FIELDS = "name title description short_intro".split()

    def __init__(self, frappe, name):
        self.frappe = frappe
        self.name = name
        self.data = self.get_data()
        self.root = Path(self.name)

    def get_data(self):
        return self.frappe.get_doc("LMS Course", self.name)

    def __repr__(self):
        return f"<Course: {self.name}>"

    def get_lessons(self):
        chapters = {c.name: c for c in self.get_chapters()}

        filters = {"chapter": ["IN", list(chapters.keys())]}
        docs = self.frappe.get_list("Lesson", filters=filters, fields=["*"])
        return [Lesson(chapters[d['chapter']], d) for d in docs]

    def get_chapters(self):
        filters = {"course": self.name}
        docs = self.frappe.get_list("Chapter", filters=filters, fields=Chapter.FIELDS)
        return [Chapter(self, d) for d in docs]

    def get_exercises(self):
        filters = {"course": self.name}
        docs = self.frappe.get_list("Exercise", filters=filters, fields=Exercise.FIELDS)
        return [Exercise(self, d) for d in docs]

    def push_exercises(self):
        root = Path(self.name)
        exercises = Exercise.load_all(course=self, root=root)
        for e in exercises:
            e.push()

    def pull(self, root="."):
        if isinstance(root, str):
            root = Path(root)

        path = root / self.name
        path.mkdir(parents=True, exist_ok=True)

        write_yaml(path / "course.yml", self.data)

        for c in self.get_chapters():
            c.pull(path)

        for doc in self.get_exercises():
            doc.pull(path)

    def push(self):
        root = Path(".")
        path = root / self.name
        for c in self.get_chapters():
            c.push(path)

    def reindex(self):
        data = {
            "course_name": self.name
        }
        invoke_method(self.frappe, "mon_school.api.reindex_course", data)

def write_yaml(path, data):
    write_file(path, yaml.safe_dump(data))

def write_file(path, contents):
    path = str(path)
    print("writing", path)
    with open(path, "w") as f:
        f.write(contents)

class Chapter:
    FIELDS = "name title course description".split()
    def __init__(self, course, data):
        self._course = course
        self.data = data
        self.__dict__.update(data)
        self.frappe = course.frappe
        self.root = self._course.root / self.name

    def get_lessons(self):
        filters = {"chapter": self.name}
        docs = self.frappe.get_list("Lesson", filters=filters, fields=["*"])
        return [Lesson(self, d) for d in docs]

    def pull(self, root="."):
        if isinstance(root, str):
            root = Path(root)

        path = root / self.name
        path.mkdir(parents=True, exist_ok=True)

        write_yaml(path / "chapter.yml", self.data)

        for lesson in self.get_lessons():
            lesson.pull(path)

    def push(self, root):
        path = root / self.name

        for lesson in self.get_lessons():
            lesson.push(path)

    def __repr__(self):
        return f"<Chapter: {self.name}>"

class Lesson(Document):
    DOCTYPE = "Lesson"
    FIELDS = "name chapter title body".split()
    def __init__(self, chapter, data):
        self.data = dict(data, chapter=chapter.name)
        self.__dict__.update(data)
        self.chapter = chapter
        self.frappe = chapter.frappe

    def __repr__(self):
        return f"<Lesson: {self.name}>"

    def pull(self, root="."):
        if isinstance(root, str):
            root = Path(root)

        path = root / (self.name + ".md")

        text = f"# {self.title}\n\n{self.body}"

        write_file(path, text)

    def push2(self, root):
        print("push", self.chapter.name, self.name)
        if isinstance(root, str):
            root = Path(root)

        path = root / (self.name + ".md")

        text = path.read_text()
        title_line, *lines = text.splitlines()

        title = title_line.strip(" #")
        body = "\n".join(lines).strip()

        assert title, f"{self.name}: missing title"
        assert body, f"{self.name}: missing body"

        doc = self.frappe.get_doc('Lesson', self.name)
        if doc['title'] == title and doc['body'].strip() == body:
            print(f"{self.name}: no changes to push...")
            return

        print("pushing...")

    @classmethod
    def load(cls, chapter: Chapter, name: str):
        filename = name + ".md"
        path = chapter.root / filename

        print("path", path)

        text = path.read_text()
        title_line, *lines = text.splitlines()

        title = title_line.strip(" #").strip()
        body = "\n".join(lines).strip()

        data = dict(name=path.stem, title=title, body=body)
        return cls(chapter=chapter, data=data)

class Exercise(Document):
    DOCTYPE = "Exercise"
    FIELDS = ["name", "title", "description", "code", "answer", "course"]

    def __init__(self, course, data):
        self._course = course
        self.data = data
        self.__dict__.update(data)
        self.frappe = course.frappe

        filename = self.name + ".yml"
        self.path = self._course.root / "exercises" / filename

    def pull(self, root="."):
        if isinstance(root, str):
            root = Path(root)

        root = root / "exercises"
        root.mkdir(parents=True, exist_ok=True)

        path = root / (self.name + ".yml")
        write_yaml(path, self.data)

    def push(self):
        """Pushes this exercise into mon.school.

        If this exercise is not present in mon.school, it will be created
        and it if already present it will be updated.
        """
        doc = {k: self.data[k] for k in self.FIELDS}
        print(f"updaing {self.name} ...")

        data = {
            "doctype": "Exercise",
            "name": self.name,
            "doc": doc
        }
        url = self.frappe.url + "/api/method/mon_school.api.save_document"
        result = self.frappe.session.post(url, json=data).json()
        message = result['message']
        if message.get("ok"):
            return message
        else:
            raise Exception(message.get("error") or f"unknown error: {message}")

    @classmethod
    def load(cls, course: Course, name: str):
        filename = name + ".yml"
        path = course.root / "exercises" / filename
        data = yaml.safe_load(path.open())
        data["name"] = path.stem
        data["course"] = course.name
        return cls(course=course, data=data)

    @classmethod
    def load_all(cls, course: Course):
        root = course.root / "exercises"
        return [cls.load(course, p.stem) for p in root.glob("*.yml")]

# https://github.com/yaml/pyyaml/issues/240
def str_presenter(dumper, data):
    try:
        dlen = len(data.splitlines())
        if (dlen > 1):
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    except TypeError:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.SafeDumper.add_representer(str, str_presenter)


class Site:
    def __init__(self, site_url):
        self.site_url = site_url

    def get_lessons(self, course):
        filters = {"course": course}
        return self.frappe.get_list("Lesson", filters=filters, fields=["*"])

@click.group()
def sync():
    pass

@sync.command()
@click.option('--site', 'site_url', default="https://mon.school", help='URL of mon.school website')
@click.option('-d', "--output_directory", help='The directory to put the files')
@click.option('--course', 'course_name', help='the course to push')
def pull(site_url, output_directory, course_name):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    course_name = course_name or COURSE_NAME
    print(course_name)

    course = Course(frappe, course_name)
    course.pull()

@sync.command()
@click.option('--site', 'site_url', default="https://mon.school", help='URL of mon.school website')
@click.option('--course', 'course_name', help='the course to push')
@click.option('--only_exercises', help='push only exercises')
def push(site_url, course_name, only_exercises=False):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    course = Course(frappe, course_name)
    if only_exercises:
        course.push_exercises()

@sync.command()
@click.option('--site', 'site_url', default="https://mon.school", help='URL of mon.school website')
@click.argument('path')
def push_exercise(site_url, path):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    p = Path(path)

    assert p.parent.name == "exercises"
    course_name = p.parent.parent.name

    course = Course(frappe, course_name)
    exercise = Exercise.load(course, name=p.stem)
    result = exercise.push()
    print(result)

@sync.command()
@click.option('--site', 'site_url', default="https://mon.school", help='URL of mon.school website')
@click.argument('path')
def push_lesson(site_url, path):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    p = Path(path)

    chapter_name = p.parent.name
    course_name = p.parent.parent.name

    course = Course(frappe, course_name)
    chapter = Chapter(course, dict(name=chapter_name))
    lesson = Lesson.load(chapter=chapter, name=p.stem)
    result = lesson.push()
    print(result)


@sync.command()
@click.option('--site', 'site_url', default="https://mon.school", help='URL of mon.school website')
@click.argument('course_name', default=COURSE_NAME)
def push_exercises(site_url, course_name):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    course = Course(frappe, course_name)
    exercises = Exercise.load_all(course)
    for e in exercises:
        result = e.push()
        print("..", result['status'])

@sync.command()
@click.argument('course_name', default=COURSE_NAME)
@click.option('--site', 'site_url', default="https://mon.school", help='URL of mon.school website')
def reindex_course(course_name, site_url):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    course = Course(frappe, course_name)
    result = course.reindex()
    print(result)

if __name__ == "__main__":
    sync()
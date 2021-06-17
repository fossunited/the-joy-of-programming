import os
import click
from frappeclient import FrappeClient
from pathlib import Path
import yaml

COURSE_NAME = "the-joy-of-programming"

API_KEY = os.getenv("FRAPPE_API_KEY")
API_SECRET = os.getenv("FRAPPE_API_SECRET")

class Course:
    FIELDS = "name title description short_intro".split()

    def __init__(self, frappe, name):
        print("Course", name)
        self.frappe = frappe
        self.name = name
        self.data = self.get_data()

        print("course", self.data)

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
        self.data = data
        self.__dict__.update(data)
        self.frappe = course.frappe

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

class Lesson:
    def __init__(self, chapter, data):
        self.data = data
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

    def push(self, root):
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

class Exercise:
    FIELDS = ["name", "title", "description", "code", "answer"]
    def __init__(self, course, data):
        self.data = data
        self.__dict__.update(data)
        self.frappe = course.frappe

    def pull(self, root="."):
        if isinstance(root, str):
            root = Path(root)

        root = root / "exercises"
        root.mkdir(parents=True, exist_ok=True)

        path = root / (self.name + ".yml")
        write_yaml(path, self.data)

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
def pull(site_url, output_directory):
    frappe = FrappeClient(site_url)
    frappe.authenticate(API_KEY, API_SECRET)

    course = Course(frappe, COURSE_NAME)
    course.pull()

if __name__ == "__main__":
    sync()
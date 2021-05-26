"""Script to generate the javascript required to put all the pieces together.
"""
from pathlib import Path
import json
import argparse
import markdown
import glob
from jinja2 import Environment, FileSystemLoader

START = Path(__file__).parent.joinpath("start.py").read_text()
SKETCH = Path(__file__).parent.joinpath("sketch.py").read_text()

# LIVECODE_BASE_URL = "https://livecode.fossunited.org"
LIVECODE_BASE_URL = "http://localhost:8010"

LIVECODE_OPTIONS = {
    "base_url": LIVECODE_BASE_URL,
    "runtime": "python",
    "files": [
        {"filename": "start.py", "contents": START},
        {"filename": "sketch.py", "contents": SKETCH},
    ],
    "command": ["python", "start.py"]
}

env = Environment(loader=FileSystemLoader("src/templates"))
env.globals['LIVECODE_BASE_URL'] = LIVECODE_BASE_URL
render = env.get_template("page.html").render

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-o", "--output", help="path to the js file to create (default: %default)", default="build/livecode_options.js")
    return p.parse_args()

def write_file(root, filename, contents):
    p = root.joinpath(filename)
    print("writing", p)
    p.write_text(contents)

def build_js(root):
    jscode = "var LIVECODE_OPTIONS = {};".format(json.dumps(LIVECODE_OPTIONS))
    write_file(root, "livecode-options.js", jscode)

def main():
    root = Path("course/assets")
    root.mkdir(exist_ok=True)
    build_js(root)

    write_file(root, "sketch.js", open("src/sketch.js").read())

if __name__ == "__main__":
    main()
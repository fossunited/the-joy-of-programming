"""Implementation macros used in the mkdocs.
"""
import hashlib
import jinja2
from pathlib import Path
import json
from urllib.parse import urlparse
import websocket
import yaml

import sys
sys.path.append("src")
from build import LIVECODE_BASE_URL, LIVECODE_OPTIONS

TEMPLATE = """
<h3> Exercise: {{title}}</h3>

{{description}}

<div class="exercise"
    data-name='{{name | tojson}}'
    data-answer='{{answer | tojson}}'
    data-code='{{code | tojson}}'
    data-image='{{image | tojson}}'
>
</div>
"""

template = jinja2.Template(TEMPLATE)

def exercise_macro(name):
    path = f"the-joy-of-programming/exercises/{name}.yml"
    exercise = yaml.safe_load(open(path))
    exercise['image'] = livecode_to_svg(exercise['answer'])
    return template.render(**exercise)

def get_livecode_ws_url():
    url = urlparse(LIVECODE_BASE_URL)
    protocol = "wss" if url.scheme == "https" else "ws"
    return protocol + "://" + url.netloc + "/livecode"

CACHE = Path("cache")
CACHE.mkdir(exist_ok=True)

def read_cache(key):
    path = CACHE / key
    return path.exists() and path.read_text() or None

def write_cache(key, value):
    if not value:
        return
    path = CACHE / key
    path.write_text(value)

def livecode_to_svg(code):
    """Renders the code as svg.
    """
    key = hashlib.sha1(code.encode('utf-8')).hexdigest()
    image = read_cache(key)
    if not image:
        print("CACHE MISS", key)
        image = _livecode_to_svg(code)
        write_cache(key, image)
    else:
        print("CACHE HIT", key)
    return image

def _livecode_to_svg(code, timeout=3):
    print("livecode", repr(code[:20]))
    try:
        ws = websocket.WebSocket()
        ws.settimeout(timeout)
        livecode_ws_url = get_livecode_ws_url()
        ws.connect(livecode_ws_url)

        msg = dict(LIVECODE_OPTIONS, msgtype="exec", code=code)
        ws.send(json.dumps(msg))

        messages = _read_messages(ws)
        commands = [m for m in messages if m['msgtype'] == 'image']
        if commands:
            return commands[0]['image']
        else:
            return ""
    except websocket.WebSocketException as e:
        print("ERROR:", e)

def _read_messages(ws):
    messages = []
    try:
        while True:
            msg = ws.recv()
            if not msg:
                break
            messages.append(json.loads(msg))
    except websocket.WebSocketTimeoutException as e:
        print("Error:", e)
        pass
    return messages

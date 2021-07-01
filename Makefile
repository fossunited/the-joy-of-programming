
.PHONY: build
build:
	python src/build.py
	PYTHONPATH=. mkdocs build

.PHONY: serve
serve:
	PYTHONPATH=. mkdocs serve -a localhost:8282

push:
	rsync -av site/* anandology.com:tmp/the-joy-of-programming/

pull:
	python frappe-sync.py pull --site https://mon.school

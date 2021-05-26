
.PHONY: build
build:
	python src/build.py
	mkdocs build

.PHONY: serve
serve:
	mkdocs serve -a localhost:8888

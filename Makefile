
.PHONY: build
build:
	python src/build.py
	mkdocs build

serve:
	mkdocs serve

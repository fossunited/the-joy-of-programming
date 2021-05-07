
.PHONY: build
build:
	python src/build.py

serve: build
	python3 -m http.server --directory build/
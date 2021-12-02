build:
	python3 -m build

deploy: build
	python3 -m twine upload dist/*
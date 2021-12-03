build:
	python3 -m build

deploy-test:
	python3 -m twine upload --repository testpypi dist/*

install-test:
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pysemble

deploy:
	python3 -m twine upload dist/*

deploy-local:
	pip install .
	pip install -e .

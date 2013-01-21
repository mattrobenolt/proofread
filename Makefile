clean:
	rm -rf *.egg-info
	rm -rf dist

publish:
	python setup.py sdist upload

test:
	cd django_tests; ./manage.py test

.PHONY: clean publish test

APP_LIST ?= card teach_to_the_cards

run:
	python manage.py runserver

install:
	pip install -r requirements/dev.txt
	npm install

test:
	@coverage run --source=. manage.py test -v2 $(APP_LIST)


ci: test
	@coverage html
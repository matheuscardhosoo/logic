all:
	poetry run isort clement-mihailescu/
	poetry run black clement-mihailescu/
	poetry run flake8 clement-mihailescu/
	poetry run mypy clement-mihailescu/ --install-types --non-interactive --show-error-codes
	poetry run pylint clement-mihailescu/

runserver:
	uvicorn main:app --reload

alembic-init:
	alembic init migrations

migrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head
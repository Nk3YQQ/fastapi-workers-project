from sqlalchemy import create_engine


def create_engine_url(postgres_settings, params: dict):
    data = postgres_settings(
        dialect=params.get('dialect'),
        user=params.get('user'),
        password=params.get('password'),
        host=params.get('host'),
        db_name=params.get('db_name'),
    )

    url = f"postgresql+{data.dialect}://{data.user}:{data.password}@{data.host}:5432/{data.db_name}"

    return create_engine(url)

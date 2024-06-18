from dataclasses import dataclass


@dataclass
class PostgresSettings:
    dialect: str
    user: str
    password: int
    host: str
    db_name: str

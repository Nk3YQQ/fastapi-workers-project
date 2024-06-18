from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self, engine):
        self.engine = engine
        self.session = sessionmaker(engine)

    def get_session(self):
        with self.session as session:
            yield session

    def create(self, instance):
        with self.session() as session:
            try:
                session.add(instance)
            except Exception as e:
                session.rollback()
                raise ValueError(f'Ошибка в добавлении сущности: {e}')
            finally:
                session.commit()

    def all(self, model):
        with self.session() as session:
            try:
                return session.query(model).all()
            except Exception as e:
                session.rollback()
                raise ValueError(f'Ошибка в чтение всех сущностей: {e}')

    def get(self, model, instance_pk: int | str):
        with self.session() as session:
            try:
                return session.get(model, instance_pk)
            except Exception as e:
                session.rollback()
                raise ValueError(f'Ошибка в чтении сущности: {e}')

    def update(self, instance, data: dict):
        with self.session() as session:
            try:
                for key, value in data.items():
                    if hasattr(instance, key) and value:
                        setattr(instance, key, value)

                session.add(instance)

            except Exception as e:
                session.rollback()
                raise ValueError(f'Ошибка в обновлении сущности: {e}')

            finally:
                session.commit()

    def delete(self, instance):
        with self.session() as session:
            try:
                session.delete(instance)

            except Exception as e:
                session.rollback()
                raise ValueError(f'Ошибка в удалении сущности: {e}')

            finally:
                session.commit()

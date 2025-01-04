from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


class DatabaseConfig:
    _instance = None
    _HOST = None
    _USER_NAME = None
    _PASSWORD = None
    _DATABASE_NAME = None
    _engine = None
    _SessionLocal = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self, HOST: str, USER_NAME: str, PASSWORD: str, DATABASE_NAME: str):
        if not self.__class__._initialized:  # Ensure __init__ is only called once
            self.__class__._HOST = HOST
            self.__class__._USER_NAME = USER_NAME
            self.__class__._PASSWORD = PASSWORD
            self.__class__._DATABASE_NAME = DATABASE_NAME
            self.__class__._engine = create_engine(self.__class__.get_database_url())
            self.__class__._SessionLocal = sessionmaker(bind=self.__class__._engine, autoflush=False, autocommit=False)
            self.__class__._initialized = True

    @classmethod
    def _check_initialized(cls):
        if not cls._initialized:
            raise Exception("DatabaseConfig not initialized. Please instantiate the DatabaseConfig class.")


    @classmethod
    def get_host(cls):
        cls._check_initialized()
        return cls._HOST

    @classmethod
    def get_user_name(cls):
        cls._check_initialized()
        return cls._USER_NAME

    @classmethod
    def get_password(cls):
        cls._check_initialized()
        return cls._PASSWORD

    @classmethod
    def get_database_name(cls):
        cls._check_initialized()
        return cls._DATABASE_NAME

    @classmethod
    def get_database_url(cls):
        cls._check_initialized()
        return f"mysql+mysqlconnector://{cls.get_user_name}:{cls.get_password}@{cls.get_host}/{cls.get_database_name}"

    @classmethod
    def get_engine(cls):
        cls._check_initialized()
        return cls._engine

    @classmethod
    @contextmanager
    def get_session(cls):
        cls._check_initialized()
        if cls._SessionLocal is None:
            raise Exception("DatabaseConfig not initialized. Please instantiate the DatabaseConfig class.")
        db = cls._SessionLocal()
        try:
            yield db
        finally:
            db.close()

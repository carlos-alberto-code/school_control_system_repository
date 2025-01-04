from conn import config
from school_control_system_repository.repository import Repository
from school_control_system_repository.models import Student, Teacher


with config.get_session() as session:
    repository = Repository[Student](model=Student, session=session)
    repository.get(Student.id == 1)

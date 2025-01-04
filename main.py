from school_control_system_repository.repository import Repository
from school_control_system_repository.config import DatabaseConfig
from school_control_system_repository.models import Student, Teacher


with DatabaseConfig.get_session() as session:
    repository = Repository[Student](model=Student, session=session)
    repository.get(Student.id == 1)

import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExerciseResponseSchema
from fixtures.courses import function_course, CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: GetExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture,
        exercises_client: ExercisesClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)

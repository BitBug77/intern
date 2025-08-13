from typing import ClassVar

class User:
    platform_name: ClassVar[str] = "EduVerse"  # Shared platform name

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name  # User's name
        self.email = email  # User's email
        self.__password = password  # Private password

    def check_password(self, password: str) -> bool:
        return self.__password == password

    def update_email(self, new_email: str) -> None:
        self.email = new_email
        print(f"Updated email: {self.email}")

    @classmethod
    def change_platform_name(cls, new_name: str) -> None:
        cls.platform_name = new_name
        print(f"Platform name changed to: {cls.platform_name}")


class Instructor(User):
    all_courses: ClassVar[list] = []  

    def __init__(self, name: str, email: str, password: str, courses: list = None) -> None:
        super().__init__(name, email, password)
        self.courses = courses if courses is not None else []

    def add_course(self, course_name: str) -> None:
        if course_name not in self.courses:
            self.courses.append(course_name)
            Instructor.all_courses.append(course_name)
            print(f"Course '{course_name}' added by {self.name}")
        else:
            print(f"Course '{course_name}' already exists for this instructor")

    def list_courses(self) -> None:
        if self.courses:
            print(f"{self.name}'s courses: {self.courses}")
        else:
            print(f"{self.name} has no courses")

    @classmethod
    def list_all_courses(cls) -> None:
        if cls.all_courses:
            print(f"All courses on platform: {cls.all_courses}")
        else:
            print("No courses available")


class Student(User):
    max_courses: ClassVar[int] = 5  

    def __init__(self, name: str, email: str, password: str, enrolled_courses: list = None) -> None:
        super().__init__(name, email, password)
        self.enrolled_courses = enrolled_courses if enrolled_courses is not None else []

    def enroll(self, course_name: str) -> None:
        if course_name not in Instructor.all_courses:
            print(f"Cannot enroll: course '{course_name}' does not exist")
        elif course_name in self.enrolled_courses:
            print(f"Already enrolled in '{course_name}'")
        elif len(self.enrolled_courses) >= self.max_courses:
            print(f"Cannot enroll in more than {self.max_courses} courses")
        else:
            self.enrolled_courses.append(course_name)
            print(f"{self.name} enrolled in '{course_name}'. Current courses: {self.enrolled_courses}")

    def drop_course(self, course_name: str) -> None:
        if course_name in self.enrolled_courses:
            self.enrolled_courses.remove(course_name)
            print(f"{self.name} dropped '{course_name}'. Remaining courses: {self.enrolled_courses}")
        else:
            print(f"Course '{course_name}' not found in enrolled courses")

user1 = User("Alice", "alice@example.com", "pass123")
print(user1.check_password("pass123"))  # True
print(user1.check_password("wrongpass"))  # False
user1.update_email("alice_new@example.com")
User.change_platform_name("EduWorld")

instructor1 = Instructor("Bob", "bob@example.com", "teach123")
instructor1.add_course("Python Basics")
instructor1.add_course("Data Science 101")

instructor2 = Instructor("Clara", "clara@example.com", "teach456")
instructor2.add_course("Web Development")
instructor2.add_course("Data Science 101")  

instructor1.list_courses()
Instructor.list_all_courses()

student1 = Student("David", "david@example.com", "stud123")
student1.enroll("Python Basics")
student1.enroll("Python Basics")  # Duplicate enrollment
student1.enroll("AI Fundamentals")  # Course doesn't exist
student1.enroll("Data Science 101")
student1.enroll("Web Development")

instructor1.add_course("Machine Learning")
student1.enroll("Machine Learning")
instructor2.add_course("Databases")
student1.enroll("Databases")
student1.enroll("Cloud Computing")  # Over limit

student1.drop_course("Python Basics")
student1.drop_course("Cyber Security")  # Not enrolled

print(student1.check_password("stud123"))  # True

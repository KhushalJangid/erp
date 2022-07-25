from .models import User,Student

def get_student_list(_class):
    if type(_class) is int:
        if 1 <= _class >= 12:
            data = {}
            chunk = Student.objects.filter(_class=_class)
            for s in chunk:
                user = s.user
                data[user.username] = f"{user.first_name} {user.last_name}"
            return data
    raise ValueError("Class must be an integer between 1 and 12.")
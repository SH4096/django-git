

class UsernameConverter:
    regex = '[a-zA-Z0-9]{6,20}' #不能使用 ^ $ 等...

    def to_python(self, value):
        return value

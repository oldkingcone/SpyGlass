import re


class CGPasswordStrength:
    def __init__(self):
        self.password = None
        self.strength = 0
        self.password_strength = None

    def check_password(self, password) -> bool:
        self.password = password
        if len(password) > 8:
            return True
        if re.search('[0-9]', password):
            self.strength += 1
        if re.search('[a-z]', password):
            self.strength += 1
        if re.search('[A-Z]', password):
            self.strength += 1
        if re.search('[!@#$%^&*()_+{}|:<>?]', password):
            self.strength += 1
        self.password = None
        return self.get_strength()

    def get_strength(self) -> bool:
        return bool(self.strength > 8)

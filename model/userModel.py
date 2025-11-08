class UserModel:
    def __init__(self, username: str, password: str):
        self._username = None
        self._password_hash = None
        self.username = username
        self.password = password

        def get_username(self) -> str:
            return self._username
        
        def set_username(self, value):
            if not value:
                raise ValueError("Username cannot be empty")
            self._username = value

        def set_password(self, raw) -> str:
            if len(password) < 6:
                raise ValueError("Password must be at least 6 characters long")
            import hashlib
            self._password_hash = hashlib.sha256(raw.encode()).hexdigest()

        username = property(get_username, set_username)
        password = property(fset=set_password)  # write-only
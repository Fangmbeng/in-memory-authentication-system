import pandas as pd

class User:
    def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):
        self.user_id = user_id
        self.username = username.lower()  # Normalize to lowercase
        self.password = password
        self.failed_attempts = failed_attempts
        self.is_locked = is_locked

    def reset_failed_attempts(self):
        self.failed_attempts = 0

    def increment_failed_attempts(self):
        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.lock_account()

    def lock_account(self):
        self.is_locked = True

class AuthenticationSystem:
    def __init__(self):
        self.users = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts", "is_locked"])

    def register_user(self, user_id, username, password):
        username = username.lower()  # Normalize username to lowercase
        if username in self.users["username"].values:
            print(f"User {username} already exists.")
            return
        
        new_user = pd.DataFrame({
            "user_id": [user_id],
            "username": [username],
            "password": [password],
            "failed_attempts": [0],
            "is_locked": [False]
        })
        self.users = pd.concat([self.users, new_user], ignore_index=True)
        print(f"User {username} registered successfully.")

    def login(self, username, password):
        username = username.lower()  # Normalize input username
        user_row = self.users[self.users['username'] == username]
        if user_row.empty:
            print(f"User {username} not found.")
            return

        user = User(user_row['user_id'].values[0], user_row['username'].values[0], user_row['password'].values[0],
                    user_row['failed_attempts'].values[0], user_row['is_locked'].values[0])

        if user.is_locked:
            print(f"Account for {username} is locked. Please contact support.")
            return

        if password == user.password:
            print(f"User {username} logged in successfully.")
            user.reset_failed_attempts()
        else:
            print(f"Failed login attempt for {username}.")
            user.increment_failed_attempts()

        self.update_user(user)

    def update_user(self, user):
        self.users.loc[self.users['username'] == user.username, 'failed_attempts'] = user.failed_attempts
        self.users.loc[self.users['username'] == user.username, 'is_locked'] = user.is_locked

# Example Usage
auth_system = AuthenticationSystem()
auth_system.register_user(1, "neena", "password123")
auth_system.register_user(2, "helios", "mysecurepassword")

# Testing case-insensitive login
auth_system.login("Neena", "password123")  # Should succeed
auth_system.login("neena", "password321")  # Should fail
auth_system.login("neena", "password321")  # Should fail
auth_system.login("neena", "password321")  # Should lock the account
auth_system.login("neena", "password123")  # Should be locked
auth_system.login("helios", "password321")  # Should fail
auth_system.login("helios", "mysecurepassword")  # Should succeed

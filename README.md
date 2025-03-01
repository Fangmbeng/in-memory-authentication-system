# in-memory-authentication-system

### Description:  
This repository implements a simple, in-memory authentication system in Python using **Pandas** for user management. The system provides basic functionalities such as user registration, login with case-insensitive username matching, tracking of failed login attempts, and automatic account locking after too many failed attempts.  

---

### Features:
- **User Registration:**  
  - Register new users with unique, case-insensitive usernames.
  
- **Login Functionality:**  
  - Authenticate users with a case-insensitive approach.
  - Reset failed login attempts upon successful login.
  - Increment failed attempts and lock the account after three consecutive failures.

- **Data Management:**  
  - Uses a Pandas DataFrame to manage user data in memory.
  - Easily extendable for persistent storage options (e.g., CSV, database).

---

### Getting Started:
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/in-memory-authentication-system.git
   cd in-memory-authentication-system
   ```
   
2. **Install Dependencies:**  
   ```bash
   pip install pandas
   ```
   
3. **Run the Script:**  
   ```bash
   python auth_system.py
   ```

---

### Usage Example:
The provided code demonstrates the following workflow:
- Registering users.
- Handling login attempts.
- Locking an account after multiple failed login attempts.
  
```python
auth_system = AuthenticationSystem()
auth_system.register_user(1, "neena", "password123")
auth_system.register_user(2, "helios", "mysecurepassword")

auth_system.login("Neena", "password123")  # Successful login (case-insensitive)
auth_system.login("neena", "password321")  # Failed login attempt
auth_system.login("neena", "password321")  # Failed login attempt
auth_system.login("neena", "password321")  # Account locked after third failure
auth_system.login("helios", "mysecurepassword")  # Successful login
```

---

### Future Enhancements:
- Integrate persistent storage (e.g., CSV, SQLite, or another database).
- Implement password hashing for enhanced security.
- Add a web-based interface for improved user interaction.

---

This project is ideal for learning the basics of authentication logic and error handling in Python. Contributions and improvements are welcome!

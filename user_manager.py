# User authentication and feedback management system
import subprocess
import sys

def install_pandas():
    try:
        import pandas
        print("pandas already installed")
    except ImportError:
        print("pandas not found… installing now")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

install_pandas()
import pandas as pd
import hashlib
import os
from datetime import datetime

USER_DATABASE = "./Data/users_database.csv"


class UserManager:
    """Handles user registration, login, and feedback"""
    
    def __init__(self):
        """Initializes user database"""
        self.database_path = USER_DATABASE
        self._initialize_database()
    
    def _initialize_database(self):
        """Creates database if it doesn't exist"""
        if not os.path.exists(self.database_path):
            df = pd.DataFrame(columns=[
                'username',
                'password_hash',
                'registration_date',
                'last_login',
                'feedback',
                'feedback_date'
            ])
            df.to_csv(self.database_path, index=False)
            print(f"✅ Created new user database: {self.database_path}")
        else:
            print(f"📂 User database found: {self.database_path}")
    
    def _hash_password(self, password):
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, password):
        """
        Registers a new user
        Returns: (success: bool, message: str)
        """
        # Validation
        if not username or not password:
            return False, "❌ Username and password cannot be empty!"
        
        if len(username) < 3:
            return False, "❌ Username must be at least 3 characters long!"
        
        if len(password) < 6:
            return False, "❌ Password must be at least 6 characters long!"
        
        # Checks if username already exists
        df = pd.read_csv(self.database_path)
        if username in df['username'].values:
            return False, f"❌ Username '{username}' already exists! Please login or choose another username."
        
        # Adds a new user
        new_user = pd.DataFrame([{
            'username': username,
            'password_hash': self._hash_password(password),
            'registration_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'last_login': '',
            'feedback': '',
            'feedback_date': ''
        }])
        
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(self.database_path, index=False)
        
        return True, f"✅ Registration successful! Welcome, {username}! You can now login."
    
    def login_user(self, username, password):
        """
        Authenticates user
        Returns: (success: bool, message: str)
        """
        if not username or not password:
            return False, "❌ Please enter both username and password!"
        
        df = pd.read_csv(self.database_path)
        
        # Checks if a user exists
        if username not in df['username'].values:
            return False, f"❌ Username '{username}' not found! Please register first."
        
        # Verifying password
        user_row = df[df['username'] == username].iloc[0]
        password_hash = self._hash_password(password)
        
        if user_row['password_hash'] != password_hash:
            return False, "❌ Incorrect password! Please try again."
        
        # Updates last login
        df.loc[df['username'] == username, 'last_login'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df.to_csv(self.database_path, index=False)
        
        return True, f"✅ Welcome back, {username}! Click 'Start Detection' to begin."
    
    def save_feedback(self, username, feedback_text):
        """
        Saves user feedback
        Returns: (success: bool, message: str)
        """
        if not feedback_text or feedback_text.strip() == "":
            return False, "❌ Feedback cannot be empty!"
        
        df = pd.read_csv(self.database_path)
        
        if username not in df['username'].values:
            return False, "❌ User session expired. Please login again."
        
        # Saves feedback
        df.loc[df['username'] == username, 'feedback'] = feedback_text
        df.loc[df['username'] == username, 'feedback_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df.to_csv(self.database_path, index=False)
        
        return True, f"✅ Thank you for your feedback, {username}! Your input has been recorded."
    
    def get_user_stats(self):
        """Get statistics about users"""
        df = pd.read_csv(self.database_path)
        return {
            'total_users': len(df),
            'users_with_feedback': len(df[df['feedback'] != ''])
        }


# Global instance
_user_manager = None

def get_user_manager():
    """Get or create user manager instance"""
    global _user_manager
    if _user_manager is None:
        _user_manager = UserManager()
    return _user_manager
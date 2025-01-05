from datetime import datetime

import jwt

from src.config import ALGORITHM, SECRET_KEY


def verify_access_token(token: str):
    """
    Verify if the provided JWT token is valid and not expired.
    Returns the decoded token payload if valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Check if the token has expired
        if payload["exp"] < datetime.now().timestamp():
            return None
        return payload  # Return the decoded token payload (usually contains user info)
    except jwt.PyJWTError:
        return None

#!/usr/bin/env python3
"""Authentication"""


from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authentication logic"""
        return False

    def authorization_header(self, request=None) -> str:
        """authentication header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None

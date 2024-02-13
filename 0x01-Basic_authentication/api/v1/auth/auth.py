#!/usr/bin/env python3
"""Authentication"""


from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authentication logic"""
        # Return True if path is None
        if path is None:
            return True

        # Return True if excluded_paths is None or empty
        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure path ends with a slash
        if not path.endswith('/'):
            path += '/'

        # Check if the path is in excluded_paths
        for excluded_path in excluded_paths:
            # Ensure excluded_path ends with a slash
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            # Check if the path starts with the excluded_path (slash-tolerant)
            if path.startswith(excluded_path):
                return False

        # If the path is not in excluded_paths, return True
        return True

    def authorization_header(self, request=None) -> str:
        """authentication header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None

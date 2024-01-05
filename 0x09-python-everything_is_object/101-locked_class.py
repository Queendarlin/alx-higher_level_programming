#!/usr/bin/python3
"""
A class LockedClass
"""


class LockedClass:
    """To prevent user from dynamically creating new instance attributes"""
    __slots__ = ('first_name')

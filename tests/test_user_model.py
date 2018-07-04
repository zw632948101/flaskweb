#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
import unittest
from app.models import User, Role
from app.models import Permissions, AnonymousUser

__author__ = 'wei.zhang'


class UserModleTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_roles_and_permissions(self):
        Role.insert_roles()
        u = User(email='john@exapmle.com', password='cat')
        self.assertTrue(u.can(Permissions.WRITE_ARTICLES))
        self.assertFalse(u.can(Permissions.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permissions.FOLLOW))

from django.test import TestCase
from django.db import models
from FindTutors.models import Profile, TUser, Room


class validUserTests(TestCase):
    def setUp(self):
        TUser.objects.create_user("TestUser", "testmail@email.com")

    def testEmail(self):
        self.assertEqual(TUser.objects.get(username="TestUser").email, "testmail@email.com")

    def testUserName(self):
        self.assertEqual(TUser.objects.get(username="TestUser").username, "TestUser")

    def testFirstName(self):
        self.assertEqual(TUser.objects.get(username="TestUser").firstname, "")

    def testLastName(self):
        self.assertEqual(TUser.objects.get(username="TestUser").lastname, "")

    def testPhone(self):
        self.assertEqual(TUser.objects.get(username="TestUser").phone_number, None)

    def testIsTutee(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_tutee, False)

    def testIsTutor(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_tutor, False)

    def testYear(self):
        self.assertEqual(TUser.objects.get(username="TestUser").year, None)

    def testSubjects(self):
        self.assertEqual(TUser.objects.get(username="TestUser").subjects, "")

    def testStaff(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_staff, False)

    def testSuperUser(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_superuser, False)

    def testIsActive(self):
        self.assertEqual(TUser.objects.get(username="TestUser").is_active, True)

    def testLastLogin(self):
        self.assertEqual(TUser.objects.get(username="TestUser").last_login, None)

class invalidUserTests(TestCase):
    def setUp(self):
        TUser.objects.create_user("test", "email@email.com")

    def testBadEmail(self):
        self.assertRaises(TypeError, TUser.objects.create_user, "TestUser")

    def testBadFirstName(self):
        self.assertRaises(TypeError, TUser.objects.get(username="test").firstname, 5)

    def testBadLastName(self):
        self.assertRaises(TypeError, TUser.objects.get(username="test").lastname, 5)

    def testBadPhone(self):
        self.assertRaises(TypeError, TUser.objects.get(username="test").phone_number, "hello")

    def testBadYear(self):
        self.assertRaises(TypeError, TUser.objects.get(username="test").year, "hello")

    def testBadSubjects(self):
        self.assertRaises(TypeError, TUser.objects.get(username="test").subjects, 5)


from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@mameste.com"
        password = "mameste123"
        user = get_user_model().objects.create_user(
                                                email=email,
                                                password=password
                                                )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email fot a new user is normalized"""
        email = "mameste@MAMESTE.com"
        user = get_user_model().objects.create_user(email, "mameste123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "mameste123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
                                                        "mameste@mameste.123",
                                                        "mameste123"
                                                        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

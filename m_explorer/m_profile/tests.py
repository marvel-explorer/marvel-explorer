from django.test import TestCase
from django.contrib.auth.models import User


class TestMarvelProfile(TestCase):
    """Test profile and user models"""
    def setUpd(self):
        self.test_user1 = User.objects.create_user(username='testuser',
                                                   email='test@test.com',
                                                   password='testpassword')
        self.test_user2 = User.objects.create_user(username='testuser2',
                                                   email='test2@test.com',
                                                   password='testpassword')
        self.test_user1.save()
        self.test_user2.save()

    def test_user_exists(self):
        """Verify user has been created."""
        self.assertEquals(len(User.objects.all()), 2)

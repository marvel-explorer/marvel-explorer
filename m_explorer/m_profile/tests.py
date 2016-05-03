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

    # def test_profile_verify(self):
    #     """Verify profile is the expected profile."""
    #     self.assertEquals(ImagerProfile.objects.all()[0],
    #                       self.test_user1.profile)
    #
    # def test_profile_user(self):
    #     """Test profile user is the expected user."""
    #     profile = ImagerProfile.objects.all()[0]
    #     self.assertEquals(profile.user, self.test_user1)
    #
    # def test_user_deletion(self):
    #     """Test when user is deleted, profile is also deleted."""
    #     self.assertEquals(len(ImagerProfile.objects.all()), 2)
    #     self.test_user1.delete()
    #     self.assertEquals(len(ImagerProfile.objects.all()), 1)
    #
    # def test_profile_deletion(self):
    #     """Test when profile is deleted, user still exists."""
    #     self.assertEquals(len(User.objects.all()), 2)
    #     self.assertEquals(len(ImagerProfile.objects.all()), 2)
    #     self.test_user2.profile.delete()
    #     self.assertEquals(len(ImagerProfile.objects.all()), 1)
    #     self.assertEquals(len(User.objects.all()), 2)
    #
    # def test_profile_active(self):
    #     """Test profile is active."""
    #     self.assertEquals(self.test_user1.profile.is_active, True)
    #
    # def test_active_profiles(self):
    #     """Test full list of active profiles is returned."""
    #     self.assertEquals(ImagerProfile.active.count(), 2)

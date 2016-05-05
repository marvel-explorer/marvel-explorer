from django.test import TestCase
from django.contrib.auth.models import User
from .models import MarvelProfile
from m_comics.models import Comic, ReadingList
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """User factory model"""
    class Meta:
        model = User


class ComicFactory(factory.django.DjangoModelFactory):
    """Comic factory model"""
    class Meta:
        model = Comic


class NewUserTestCase(TestCase):
    def setUp(self):
        self.beast = UserFactory.create(
            username='beast',
            email='beast@xmen.com'
            )
        self.beast.set_password('xavier')
        self.cyclops = UserFactory.create(
            username='cyclops',
            email='cyclops@xmen.com'
            )
        self.cyclops.set_password('xavier')
        self.rogue = UserFactory.create(
            username='rogue',
            email='rogue@xmen.com'
            )
        self.rogue.set_password('xavier')

    def test_users_exist(self):
        self.assertTrue(self.beast)
        self.assertTrue(self.cyclops)
        self.assertTrue(self.rogue)

    def test_users_have_profile(self):
        self.assertTrue(self.beast.profile)
        self.assertTrue(self.cyclops.profile)
        self.assertTrue(self.rogue.profile)

    def test_user_has_readinglist(self):
        self.assertTrue(self.beast.readinglist)
        self.assertTrue(self.cyclops.readinglist)
        self.assertTrue(self.rogue.readinglist)

    def test_readinglist_has_comics(self):

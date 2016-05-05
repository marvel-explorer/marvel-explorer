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
        self.assertTrue(self.beast.readinglist.comics)
        self.assertTrue(self.cyclops.readinglist.comics)
        self.assertTrue(self.rogue.readinglist.comics)

    def test_profile_has_bio(self):
        self.assertEquals(self.beast.profile.bio, '')
        self.assertEquals(self.cyclops.profile.bio, '')
        self.assertEquals(self.rogue.profile.bio, '')

    def test_profile_has_favorite_hero(self):
        self.assertEquals(self.beast.profile.fav_hero, '')
        self.assertEquals(self.cyclops.profile.fav_hero, '')
        self.assertEquals(self.rogue.profile.fav_hero, '')

    def test_profile_has_location(self):
        self.assertEquals(self.beast.profile.location, '')
        self.assertEquals(self.cyclops.profile.location, '')
        self.assertEquals(self.rogue.profile.location, '')

    def test_num_users(self):
        self.assertEquals(len(User.objects.all()), 3)

    def test_num_profiles(self):
        self.assertEquals(len(MarvelProfile.objects.all()), 3)

    def test_num_readinglists(self):
        self.assertEquals(len(ReadingList.objects.all()), 3)

    def test_usernames(self):
        self.assertEquals(self.beast.username, 'beast')
        self.assertEquals(self.cyclops.username, 'cyclops')
        self.assertEquals(self.rogue.username, 'rogue')

    def test_emails(self):
        self.assertEquals(self.beast.email, 'beast@xmen.com')
        self.assertEquals(self.cyclops.email, 'cyclops@xmen.com')
        self.assertEquals(self.rogue.email, 'rogue@xmen.com')

    def test_user_pk_matches_profile_pk(self):
        self.assertEquals(self.beast.pk, self.beast.profile.pk,)
        self.assertEquals(self.cyclops.pk, self.cyclops.profile.pk,)
        self.assertEquals(self.rogue.pk, self.rogue.profile.pk,)


class NewUserUnsavedCase(TestCase):
    def setUp(self):
        self.wasp = UserFactory.build(
            username='wasp',
            email='janet@avengers.com'
        )
        self.wasp.set_password('avengers')
        self.antman = UserFactory.build(
            username='antman',
            email='hank@avengers.com'
        )
        self.antman.set_password('avengers')

    def test_unsaved_user_exists(self):
        self.assertTrue(self.antman)
        self.assertTrue(self.wasp)

    def test_unsaved_no_profile(self):
        self.assertIsNone(self.antman.profile)
        self.assertIsNone(self.wasp.profile)

    def test_unsaved_no_readinglist(self):
        with self.assertRaises(self.DoesNotExist):
            self.antman.readinglist
        with self.assertRaises(self.DoesNotExist):
            self.wasp.readinglist

    def test_unsaved_no_id(self):
        self.assertIsNone(self.antman.id)
        self.assertIsNone(self.wasp.id)

from django.test import TestCase
from django.contrib.auth.models import User
from .models import MarvelProfile
from m_comics.models import Comic, ReadingList
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient, APITestCase


import factory


class UserFactory(factory.django.DjangoModelFactory):
    """User factory model"""
    class Meta:
        model = User


class ComicFactory(factory.django.DjangoModelFactory):
    """Comic factory model"""
    class Meta:
        model = Comic


class NewComicTestCase(TestCase):
    """Testing new comics added to the db"""
    def setUp(self):
        self.testcomic1 = Comic(
            marvel_id=42882,
            title='Lorna the Jungle Girl (1954) #6',
            issue_number=6,
            page_count=32,
        )
        self.testcomic1.save()

        self.testcomic2 = Comic(
            marvel_id=41530,
            title='Ant-Man: So (Trade Paperback)',
            issue_number=0,
            page_count=136,
        )
        self.testcomic2.save()

        self.deadpool = UserFactory.create(
            username='deadpool',
            email='wade@wilson.com'
        )
        self.deadpool.set_password('chimichanga')

    def test_comics_exist(self):
        self.assertTrue(self.testcomic1)
        self.assertTrue(self.testcomic2)

    def test_comics_title(self):
        self.assertEquals(
            self.testcomic1.title,
            'Lorna the Jungle Girl (1954) #6'
        )
        self.assertEquals(
            self.testcomic2.title,
            'Ant-Man: So (Trade Paperback)'
        )

    def test_comics_pk(self):
        self.assertEquals(self.testcomic1.marvel_id, 42882)
        self.assertEquals(self.testcomic2.marvel_id, 41530)

    def test_num_comics(self):
        self.assertEquals(len(Comic.objects.all()), 2)

    def test_default_or_null_fields(self):
        self.assertEquals(self.testcomic1.detail_url, None)
        self.assertEquals(self.testcomic1.description, '')
        self.assertEquals(self.testcomic1.purchase_url, None)
        self.assertEquals(self.testcomic2.str_pur_date, None)
        self.assertEquals(self.testcomic2.upc, None)
        self.assertEquals(self.testcomic2.purchase_date, None)


class NewUserTestCase(TestCase):
    """Testing new users added to the db"""
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

    def test_unsaved_no_id(self):
        self.assertIsNone(self.antman.id)
        self.assertIsNone(self.wasp.id)


class AuthSecurityTest(APITestCase):
    """Test routes with authentication."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.spiderman = UserFactory.create(
            username='spiderman',
            email='peter@parkerindustries.com',
            password='newyork'
        )
        token = Token.objects.get(user__username='spiderman')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.spiderman.profile.bio = """While attending a public exhibition
            demonstrating the safe handling of nuclear laboratory
            waste materials, sponsored by the General Techtronics Corporation,
            the 15-year-old Peter Parker was bitten on the hand by a spider
            that had been irradiated by a particle
            accelerator used in the demonstration."""

    def test_auth_user_get(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_profile_get(self):
        response = self.client.get('/users/profile')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_comics_get(self):
        response = self.client.get('/users/comics')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_profile_post(self):
        response = self.client.put(
            '/users/profile', {
                'location': 'New York, NY'
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_herofinder(self):
        response = self.client.get('/herofinder/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UnauthSecurityTest(APITestCase):
    """Test routes without authentication."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_unauth_signin_get(self):
        response = self.client.get('/users/signup')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth_herofinder_get(self):
        response = self.client.get('/herofinder/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth_user_get(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauth_profile_get(self):
        response = self.client.get('/users/profile')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauth_comics_get(self):
        response = self.client.get('/users/comics')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauth_user_post(self):
        response = self.client.post('/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauth_profile_post(self):
        response = self.client.post('/users/profile')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauth_comics_post(self):
        response = self.client.post('/users/comics')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

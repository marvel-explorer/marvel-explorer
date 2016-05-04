"""Testing the character models."""
from django.test import TestCase
from questions.models import Character


# class CharacterFactory(factory.django.DjangoModelFactory):
#     """Define a User factory with a single user."""

#     class Meta:
#         """Define a model instance class."""

#         model = Character

#     marvel_id = "123456"
#     marvel_name = "Bob"


class CharacterTestCase(TestCase):
    """Define a class with a series of image tests."""

    def setUp(self):
        """Instance setup factory."""
        self.character = Character(marvel_id="12345", marvel_name="Bob", total_comics=8)
        self.character.save()

    def test_character(self):
        """Test that chracter manager connection is made."""
        self.assertTrue(self.character.marvel_id, '12345')

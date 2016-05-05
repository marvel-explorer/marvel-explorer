"""Testing the character models."""
from django.test import TestCase
from questions.models import Character
import factory


class CharacterFactory(factory.django.DjangoModelFactory):
    """Define a User factory with a single user."""

    class Meta:
        """Define a model instance class."""

        model = Character

    marvel_id = "123456"
    marvel_name = "Mega_Marvel_Man"
    total_comics = 9


class CharacterTestCase(TestCase):
    """Define a class with a series of image tests."""

    def setUp(self):
        """Instance setup factory."""
        self.character = CharacterFactory()
        self.character.save()

    def test_character_id(self):
        """Test that chracter attribute is assigned."""
        self.assertTrue(self.character.marvel_id, '12345')

    def test_character_name(self):
        """Test that chracter attribute is assigned."""
        self.assertTrue(self.character.marvel_name, 'Mega_Marvel_Man')

    def test_character_total_comics(self):
        """Test that chracter attribute is assigned."""
        self.assertTrue(self.character.total_comics, 9)

    def test_character_golden(self):
        """Test that chracter attribute is assigned."""
        # import pdb; pdb.set_trace()
        self.assertFalse(self.character.golden, None)


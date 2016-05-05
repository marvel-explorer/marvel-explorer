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
        self.assertEquals(self.character.golden, None)

    def test_character_silver(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.silver, None)

    def test_character_bronze(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.bronze, None)
    
    def test_character_dark(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.dark, None)

    def test_character_modern(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.modern, None)

    def test_character_clean_name(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.name, '')

    def test_character_description(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.description, '')

    def test_character_thumbnail(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.thumbnail, '')

    def test_character_gender(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.gender, '')

    def test_character_pob(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.pob, '')

    def test_character_citizenship(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.citizenship, '')

    def test_character_occupation(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.occupation, '')

    def test_character_powers(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.powers, '')

    def test_character_hair(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.hair, '')

    def test_character_eyes(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.eyes, '')

    def test_character_first_appearance(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.first_appearance, '')

    def test_character_identity_status(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.identity_status, '')

    def test_character_aliases(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.aliases, '')

    def test_character_weight(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.weight, '')

    def test_character_height(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.height, '')

    def test_character_group_aff(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.group_aff, '')

    def test_character_paraphernalia(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.paraphernalia, '')

    def test_character_education(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.education, '')

    def test_character_abilities(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.abilities, '')

    def test_character_weapons(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.weapons, '')

    def test_character_origin(self):
        """Test that chracter attribute is assigned."""
        self.assertEquals(self.character.origin, '')

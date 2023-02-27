from django.test import TestCase
from django.contrib.auth.models import User
from .models import Group

class GroupModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.group = Group.objects.create(owner=self.user1, name='Test Group')
        self.group.members.add(self.user1)
        self.group.members.add(self.user2)

    def test_group_creation(self):
        self.assertTrue(isinstance(self.group, Group))
        self.assertEqual(str(self.group), f'{self.user1} Test Group')

    def test_group_members(self):
        self.assertEqual(self.group.members.count(), 2)
        self.assertIn(self.user1, self.group.members.all())
        self.assertIn(self.user2, self.group.members.all())

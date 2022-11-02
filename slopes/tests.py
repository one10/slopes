import django
from django.test import TestCase

client = django.test.Client()


class BasicTests(TestCase):
    def test_super_basic(self) -> None:
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        response_body_str = response.content.decode("utf-8")
        self.assertGreater(len(response_body_str), 1)

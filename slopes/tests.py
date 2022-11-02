import django
from django.db import IntegrityError
from django.test import TestCase
from django.utils import timezone

from slopes.models import (Slope, SlopeUpdate, SlopeUpdateStatus,
                           SlopeUpdateType)

client = django.test.Client()


class BasicTests(TestCase):
    def test_super_basic_view_test(self) -> None:
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        response_body_str = response.content.decode("utf-8")
        self.assertGreater(len(response_body_str), 1)

    def test_super_basic_model_test1(self) -> None:
        slope1 = Slope(name="brr")
        slope1.save()
        slope1.refresh_from_db()
        self.assertEqual(slope1.name, "brr")
        self.assertIsNotNone(slope1.created_at)
        self.assertIsNotNone(slope1.updated_at)

        slope_update1 = SlopeUpdate()
        slope_update1.type = SlopeUpdateType.SEASON_OPENING.value
        slope_update1.status = SlopeUpdateStatus.APPROXIMATE.value
        with self.assertRaises(IntegrityError):
            slope_update1.save()

    def test_super_basic_model_test2(self) -> None:
        slope1 = Slope(name="brr")
        slope1.save()
        slope1.refresh_from_db()
        self.assertEqual(slope1.name, "brr")
        self.assertIsNotNone(slope1.created_at)
        self.assertIsNotNone(slope1.updated_at)

        slope_update1 = SlopeUpdate()
        slope_update1.type = SlopeUpdateType.SEASON_OPENING.value
        slope_update1.status = SlopeUpdateStatus.APPROXIMATE.value
        slope_update1.slope = slope1
        slope_update1.effective_date = timezone.now()
        slope_update1.save()

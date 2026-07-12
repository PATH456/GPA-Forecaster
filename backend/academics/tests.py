from django.test import TestCase

from .models import Term


class HealthCheckApiTests(TestCase):
    def test_health_check(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class TermApiTests(TestCase):
    def test_list_terms(self):
        Term.objects.create(season=Term.Season.FALL, year=2026)
        Term.objects.create(season=Term.Season.SPRING, year=2027)

        response = self.client.get("/api/terms/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [
                {"id": 2, "season": "spring", "year": 2027},
                {"id": 1, "season": "fall", "year": 2026},
            ],
        )

    def test_create_term(self):
        response = self.client.post(
            "/api/terms/",
            data={"season": "fall", "year": 2026},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["season"], "fall")
        self.assertEqual(response.json()["year"], 2026)
        self.assertTrue(Term.objects.filter(season="fall", year=2026).exists())

    def test_reject_duplicate_term(self):
        Term.objects.create(season=Term.Season.FALL, year=2026)

        response = self.client.post(
            "/api/terms/",
            data={"season": "fall", "year": 2026},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Term.objects.count(), 1)

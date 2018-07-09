from django.test import TestCase
from model_mommy import mommy

from core.models import Carousel


class IndexViewTest(TestCase):
    def test_get_home_success_url(self):
        response = self.client.get('/#/')

        self.assertEqual(response.status_code, 200)

    def test_get_about_success_url(self):
        response = self.client.get('/#/about')

        self.assertEqual(response.status_code, 200)

    def test_get_carousel_success_url(self):
        response = self.client.get('/#/carousel')

        self.assertEqual(response.status_code, 200)

    def test_get_contact_us_success_url(self):
        response = self.client.get('/#/contact')

        self.assertEqual(response.status_code, 200)


class APITest(TestCase):
    def test_get_carousels_success_url(self):
        response = self.client.get('/api/carousels/')

        self.assertEqual(response.status_code, 200)

    def test_post_carousels_success_url(self):
        response = self.client.post(
            '/api/carousels/',
            {
                'title': 'Slide 1',
                'description': 'For more sliders'
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_update_carousels_success_url(self):
        carousel = mommy.make(
            Carousel,
            title='Slide 20',
            description='Slide 10 update'

        )
        response = self.client.put(
            '/api/carousels/{}/'.format(carousel.id),
            {
                'title': 'Slide 10',
                'description': 'Slide 10 update',
                'is_completed': True
            }

        )

        self.assertEqual(response.status_code, 415)

    def test_delete_carousels_success_url(self):
        carousel = mommy.make(Carousel)
        response = self.client.delete(
            '/api/carousels/{}/'.format(carousel.id)
        )

        self.assertEqual(response.status_code, 204)

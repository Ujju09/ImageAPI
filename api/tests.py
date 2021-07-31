from django.test import TestCase
# API TESTING
from django.urls import reverse
from rest_framework import status

from .models import Image, Language, Tags
from .serializers import ImageSerializer


# from rest_framework.test import APITestCase,URLPatternsTestCase


# noinspection PyUnresolvedReferences
class ModelsTestCase(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.tag = Tags.objects.create(tag_name='TestTag1')
        cls.tag2 = Tags.objects.create(tag_name='TestTag2')
        cls.lang = Language.objects.create(name='Urdu')
        cls.lang2 = Language.objects.create(name='TestLang')
        cls.image = Image.objects.create(name='testname', image_asset='asset.svg', language=cls.lang, tag=cls.tag)
        cls.image2 = Image.objects.create(name='testname1', image_asset='asset1.svg', language=cls.lang2, tag=cls.tag2)

    # tear downs

    def test_tag_model(self):
        tag1 = Tags.objects.get(id=1)
        tag2 = Tags.objects.get(id=2)
        expected_tag_name1 = f"{self.tag.tag_name}"
        expected_tag_name2 = f"{self.tag2.tag_name}"
        self.assertEqual(expected_tag_name1, tag1.tag_name)
        self.assertEqual(expected_tag_name2, tag2.tag_name)

    def test_language_model(self):
        lang1 = Language.objects.get(id=1)
        expected_lang_name = f"{self.lang.name}"
        self.assertEqual(expected_lang_name, lang1.name)

    def test1_image_models(self):
        self.assertEqual(self.image.tag, self.tag)
        self.assertEqual(self.image.name, "testname")
        self.assertEqual(self.image.language, self.lang)
        self.assertEqual(self.image.image_asset, "asset.svg")

    def test2_iamge_models(self):
        self.assertEqual(self.image2.tag, self.tag2)
        self.assertEqual(self.image2.name, "testname1")
        self.assertEqual(self.image2.language, self.lang2)
        self.assertEqual(self.image2.image_asset, "asset1.svg")

    def test_get_all_images_api(self):
        response = self.client.get(reverse(
            'assets'))  # api response : I was getting errors here, fixed by using  name ='assets' kwarg in api.urls
        # and now it works
        print(reverse('assets'))
        # Status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assets = Image.objects.all()
        serializer = ImageSerializer(assets, many=True)
        # Serializer stores image in a different format
        comparing_props = ["name", "language", "tag"]
        for i in range(2):
            for c in comparing_props:
                self.assertEqual(response.data[i][c], serializer.data[i][c])

    # Detaill view test: when json is present
    def test_detail_api_calls(self):
        response1 = self.client.get(reverse("image-detail", kwargs={'pk': self.image.pk}))
        response2 = self.client.get(reverse("image-detail", kwargs={'pk': self.image2.pk}))

        # URL verification
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        # data verification
        asset1 = Image.objects.get(id=1)
        asset2 = Image.objects.get(id=2)
        serializer1 = ImageSerializer(asset1)
        serializer2 = ImageSerializer(asset2)
        comparing_props = ["name", "language", "tag"]
        for c in comparing_props:
            self.assertEqual(serializer1.data[c], response1.data[c])
            self.assertEqual(serializer2.data[c], response2.data[c])

    # Detaill view test: when json is absent
    def test_detail_api_calls_noJson(self):
        response1 = self.client.get(reverse("image-detail", kwargs={'pk': int(3)}))
        self.assertEqual(response1.status_code, status.HTTP_404_NOT_FOUND)

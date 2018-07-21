from django.test import TestCase
from onlineapp.models import *
from onlineapp.serilalizers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


# Create your tests here.
class onlineappTestCase(TestCase):
    def setUp(self):
        self.testcase1()

    def testcase1(self):
        college = College(name="Gayatri Vidhya Parishad", acronym="GVP", location="vizag",
                          contact="bhanuteja2696@gmail.01com")
        serializer = CollegeSerializer(college)

        content = JSONRenderer().render(serializer.data)
        # deserialize
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = CollegeSerializer(data=data)
        serializer.is_valid()
        result = serializer.save()
        self.assertEqual(college.name, result.name)

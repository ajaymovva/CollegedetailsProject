from django.db import models

from onlineapp.models import *


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'location', 'acronym', 'contact')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'dob', 'email', 'db_folder', 'dropped_out', 'college')


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTestMarks
        fields = ('problem1', 'problem2', 'problem3', 'problem4', 'total')


class StudentDetail(serializers.ModelSerializer):
    mocktestmarks = MarksSerializer()

    class Meta:
        model = Student
        fields = ('name', 'dob', 'email', 'db_folder', 'dropped_out', 'college', 'mocktestmarks')

    def create(self, validated_data):
        # import ipdb
        # ipdb.set_trace()
        profile_data = validated_data.pop('mocktestmarks')
        user = Student.objects.create(**validated_data)
        MockTestMarks.objects.create(student=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        mocktestmarks_data = validated_data.pop('mocktestmarks')
        mocktestmarks = instance.mocktestmarks
        instance.name = validated_data['name']
        instance.dob = validated_data['dob']
        instance.email = validated_data['email']
        instance.db_folder = validated_data['db_folder']
        instance.dropped_out = validated_data['dropped_out']
        instance.college = validated_data['college']

        instance.mocktestmarks.problem1 = mocktestmarks_data['problem1']
        instance.mocktestmarks.problem2 = mocktestmarks_data['problem2']
        instance.mocktestmarks.problem3 = mocktestmarks_data['problem3']
        instance.mocktestmarks.total = mocktestmarks_data['total']
        instance.mocktestmarks.problem4 = mocktestmarks_data['problem4']
        instance.mocktestmarks.save()
        instance.save()
        return instance

# # class CollegeSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = College
# #         fields = ('name', 'location', 'acronym', 'contact')
#
#
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('name', 'db_folder', 'email', 'dob', 'dropped_out')
#
#
# class MockTest1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = MockTestMarks
#         fields = ('problem1', 'problem2', 'problem3', 'problem4')
#
#
# class StudentDetailSerializer(serializers.ModelSerializer):
#     mocktestmarks = MockTest1Serializer()
#
#     class Meta:
#         model = Student
#         fields = ('name', 'db_folder', 'email', 'dob', 'dropped_out', 'mocktestmarks')
#
#     # def create(self,validated_data):
#     #     mock_data = validated_data.pop('mocktest1')
#     #     student = Student.objects.create(**validated_data)
#     #     import ipdb
#     #     ipdb.set_trace()
#     #     #MockTest1.objects.create(student__id = student_id,mock_data)
#     #
#     #     return student
#
#
#     def update(self, instance, validated_data):
#         mock_data = validated_data.pop('mocktestmarks')
#         mocktest = instance.mocktest1
#         instance.__dict__.update(**validated_data)
#         instance.save()
#         mocktest.__dict__.update(mock_data)
#         mocktest.total = int(mocktest.problem1) + int(mocktest.problem2) + int(mocktest.problem3) + int(
#             mocktest.problem4)
#         mocktest.save()
#         return instance

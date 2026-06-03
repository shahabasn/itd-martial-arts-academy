from rest_framework import serializers

from .models import Student, Batch


class StudentSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Student

        fields = '__all__'


class BatchSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Batch

        fields = '__all__'
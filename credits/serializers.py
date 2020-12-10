from rest_framework import serializers
from .checks import run_checks
from .models import Application, Blacklist, Borrower, Program
from .utils import parse_birth_date


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['name', 'min_sum', 'max_sum', 'min_age', 'max_age']


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['iin', 'date_of_birth']
        read_only_fields = ['date_of_birth']

    def create(self, validated_data):
        validated_data['date_of_birth'] = parse_birth_date(validated_data['iin'])
        return Borrower.objects.create(**validated_data)


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['program', 'borrower', 'value', 'status', 'refusing_reason']
        read_only_fields = ['status', 'refusing_reason']

    def create(self, validated_data):
        application = Application(**validated_data)

        status, error = run_checks(application, application.program)
        application.status = status
        application.refusing_reason = error
        application.save()

        return application


class BlacklistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['iin']

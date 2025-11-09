from rest_framework import  serializers
from notes.models import Note
from django.contrib.auth.models import User

class  NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user  = User.objects.create_user(**validated_data)
        return user
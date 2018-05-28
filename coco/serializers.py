from rest_framework import serializers
from cocoapp.models import User, Saving

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SavingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'
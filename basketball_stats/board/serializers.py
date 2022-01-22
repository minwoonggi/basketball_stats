from user.models import BsUser
from rest_framework import serializers

class BsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BsUser
        fields = '__all__' # 필드 지정 안하면 모든 필드
        
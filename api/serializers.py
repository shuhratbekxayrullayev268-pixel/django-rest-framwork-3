from rest_framework.serializers import ModelSerializer
from .models import Telefon


class TelefonSeralizer(ModelSerializer):

    class Meta:

        model = Telefon
        fields = ["id", "name"]

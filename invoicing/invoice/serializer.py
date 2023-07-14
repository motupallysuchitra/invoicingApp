from rest_framework import serializers
from .models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class Itemserializers(serializers.ModelSerializer):
        class Meta:
                model=Items
                fields=["desc","rate","quantity"]

class InvoicesSerializer(serializers.ModelSerializer):
    items=Itemserializers(many=True)

    class Meta:
        model=Invoices
        fields="__all__"    
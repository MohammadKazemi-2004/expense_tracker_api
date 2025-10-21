from .models import Expense
from rest_framework import serializers

class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ["owner"]
    
    

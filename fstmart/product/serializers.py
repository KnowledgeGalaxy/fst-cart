# serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'imageUrl']


# serializers.py


from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
# serializers.py


# serializers.py


from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'age', 'password', 'confirm_password']

    def validate(self, data):
        # Add your password validation logic here
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        # You can add more password validation logic here if needed

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return Customer.objects.create(**validated_data)


from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','address_type', 'street', 'city', 'state', 'zip_code' ,'contact_number']


# serializers.py
from .models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['customer_id', 'password']


# serializers.py
from rest_framework import serializers
from .models import OrderedItems, ConfirmOrder



class OrderedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItems
        fields = ['id', 'product_id', 'customer_id', 'quantity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product_id'] = instance.product_id.id
        return representation

class ConfirmOrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
    order_id = serializers.PrimaryKeyRelatedField(queryset=OrderedItems.objects.all())

    class Meta:
        model = ConfirmOrder
        fields = ['id', 'customer_id', 'address', 'contact_number', 'created_at', 'updated_at', 'order_id']

from .models import BillDetails

# serializers.py
# serializers.py
from rest_framework import serializers
from .models import BillDetails

class BillSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), default="9999999999")
    ordered_items = serializers.PrimaryKeyRelatedField(many=True, queryset=OrderedItems.objects.all())

    class Meta:
        model = BillDetails
        fields = ['id', 'ordered_items','customer_id', 'total_cost', 'created_at']
        
# serializers.py

from rest_framework import serializers
from .models import ProductFeedback, WebsiteFeedback

class ProductFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeedback
        fields = ['product_id', 'feedback_text', 'rating']

    # Override create method to handle product_id
    def create(self, validated_data):
        product_id = validated_data.pop('product_id')
        feedback = ProductFeedback.objects.create(product_id_id=product_id, **validated_data)
        return feedback

class WebsiteFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteFeedback
        fields = ['id', 'feedback_text', 'rating', 'customer_id' , 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['customer_id'] = instance.customer_id.customer_id
        return representation
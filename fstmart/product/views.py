from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer
from .models import Customer
from .serializers import CustomerSerializer


class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)


# views.py




# views.py

from .models import Customer
from .serializers import CustomerSerializer

class CustomerListCreateView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            # Save the customer object
            customer = serializer.save()

            # Return the serialized customer object in the response
            response_data = {
                "message": "Customer created successfully",
                "customer": serializer.data,  # Serialize the customer data
                # Add other fields you want to include in the response
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get_object(self, customer_id):
        try:
            return Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, customer_id, format=None):
        customer = self.get_object(customer_id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, customer_id, format=None):
        customer = self.get_object(customer_id)
        serializer = CustomerSerializer(customer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id, format=None):
        customer = self.get_object(customer_id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from .models import Address, Customer
from .serializers import AddressSerializer

class AddressList(APIView):
    def get(self, request, customer_id, format=None):
        addresses = Address.objects.filter(customer__customer_id=customer_id)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request, customer_id, format=None):
        customer = Customer.objects.get(customer_id=customer_id)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetail(APIView):
    def get_object(self, customer_id, address_id):
        try:
            return Address.objects.get(customer__customer_id=customer_id, id=address_id)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, customer_id, address_id, format=None):
        address = self.get_object(customer_id, address_id)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, customer_id, address_id, format=None):
        address = self.get_object(customer_id, address_id)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id, address_id, format=None):
        address = self.get_object(customer_id, address_id)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressDetailById(APIView):
    def get_object_by_id(self, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, address_id, format=None):
        address = self.get_object_by_id(address_id)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

# views.py
# views.py

from django.contrib.auth.hashers import check_password
from .models import Customer
from .serializers import LoginSerializer

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            customer_id = serializer.validated_data['customer_id']
            password = serializer.validated_data['password']

            # Check if the customer_id exists in the Customer model
            try:
                customer = Customer.objects.get(customer_id=customer_id)

                # Check if the provided password matches the stored password
                if password == customer.password:
                    # Return customer details in the response body
                    response_data = {
                        "message": "Login successful",
                        "customer_id": customer.customer_id,
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)

            except Customer.DoesNotExist:
                return Response({"message": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  OrderedItems, ConfirmOrder
from .serializers import OrderedItemsSerializer, ConfirmOrderSerializer

class OrderedItemsAPIView(APIView):
    def get(self, request):
        ordered_items = OrderedItems.objects.all()
        serializer = OrderedItemsSerializer(ordered_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderedItemsSerializer(data=request.data, many=True)
        return self.handle_serializer(serializer)

    def put(self, request):
        ordered_items = OrderedItems.objects.all()
        serializer = OrderedItemsSerializer(ordered_items, data=request.data, many=True)
        return self.handle_serializer(serializer)

    def delete(self, request):
        ordered_items = OrderedItems.objects.all()
        ordered_items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def handle_serializer(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderedItemsDetailAPIView(APIView):
    def get_object(self, item_id):
        try:
            return OrderedItems.objects.get(id=item_id)
        except OrderedItems.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, item_id):
        ordered_item = self.get_object(item_id)
        serializer = OrderedItemsSerializer(ordered_item)
        return Response(serializer.data)

    def put(self, request, item_id):
        ordered_item = self.get_object(item_id)
        serializer = OrderedItemsSerializer(ordered_item, data=request.data)
        return self.handle_serializer(serializer)

    def delete(self, request, item_id):
        ordered_item = self.get_object(item_id)
        ordered_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def handle_serializer(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmOrderAPIView(APIView):
    def get(self, request):
        confirm_orders = ConfirmOrder.objects.all()
        serializer = ConfirmOrderSerializer(confirm_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConfirmOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConfirmOrderDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return ConfirmOrder.objects.get(id=id)
        except ConfirmOrder.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        confirm_order = self.get_object(id)
        serializer = ConfirmOrderSerializer(confirm_order)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        confirm_order = self.get_object(id)
        serializer = ConfirmOrderSerializer(confirm_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        confirm_order = self.get_object(id)
        confirm_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BillDetails
from .serializers import BillSerializer

# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BillDetails
from .serializers import BillSerializer

# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BillDetails
from .serializers import BillSerializer

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BillDetails
from .serializers import BillSerializer

class BillAPIView(APIView):
    def post(self, request):
        ordered_items_data = request.data.get('ordered_items', [])
        serializer = BillSerializer(data=request.data)

        if serializer.is_valid():
            # Save the Bill instance after calculating total_cost
            bill_instance = serializer.save()

            return Response(BillSerializer(bill_instance).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductFeedback, WebsiteFeedback
from .serializers import ProductFeedbackSerializer, WebsiteFeedbackSerializer

class ProductFeedbackAPIView(APIView):
    def get(self, request, product_id):
        feedback = ProductFeedback.objects.filter(product_id=product_id)
        serializer = ProductFeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        serializer = ProductFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product_id=product_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WebsiteFeedbackAPIView(APIView):
    def get(self, request):
        feedback = WebsiteFeedback.objects.all()
        serializer = WebsiteFeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WebsiteFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebsiteFeedbackDetailAPIView(APIView):
    def get(self, request, pk):
        feedback = self.get_object(pk)
        serializer = WebsiteFeedbackSerializer(feedback)
        return Response(serializer.data)

    def put(self, request, pk):
        feedback = self.get_object(pk)
        serializer = WebsiteFeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        feedback = self.get_object(pk)
        serializer = WebsiteFeedbackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        feedback = self.get_object(pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return WebsiteFeedback.objects.get(pk=pk)
        except WebsiteFeedback.DoesNotExist:
            raise Http404
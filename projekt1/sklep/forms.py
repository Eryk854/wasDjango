from django.forms import ModelForm

from .models import Order,Complaint


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'delivery']

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['name','message']

from django.urls import path

from .views import MembershipSelectView, PaymentView

app_name = 'memeberships'

urlpatterns = [
	path('', MembershipSelectView.as_view(),name='select'),
	path('payment', PaymentView,name='payment')
]
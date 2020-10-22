from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Index, PricingView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('pricing/', PricingView.as_view(), name='pricing'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pre-order/', views.pre_order),
    path('success/', views.SuccessView.as_view()),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),


]

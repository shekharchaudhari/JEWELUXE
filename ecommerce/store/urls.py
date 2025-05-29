from django.urls import path
from . import views
from .views import product_list,home,product_detail,signup,custom_logout

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('signup/', views.signup, name='signup'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('login/', views.login, name='login'),
    path('test-msg/', views.test_message),


]

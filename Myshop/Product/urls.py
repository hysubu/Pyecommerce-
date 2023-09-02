from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home , name="home"),
    path("shopping/", views.shopping , name="shopping"),
    path("viewproduct/<int:id>/", views.viewproduct , name="viewproduct"),
    path("cartpage/", views.cartpage , name="cartpage"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("increase/", views.increate_item, name="increase-product"),
    path("decrease/", views.decrease_item, name="decrease-product"),
    path("cartitem/", views.remove_cart_item, name="delete-cart-item"),
    path("buynow/", views.buy_now, name="buynow"),
    path("selectaddress/", views.select_address, name="select-address"),
    path("addaddress/", views.add_order_address, name="add-address"),
    path("changeaddress/", views.change_address, name="change-address"),
    path("cashondelivery/", views.cash_on_delivery, name="cod"),
    path("customerservices/", views.customerservice, name="customer-services"),
    path("razorpays/", views.razor_pay, name="razorpay"),
    path("successfull/", views.payment_success, name="success-payment"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
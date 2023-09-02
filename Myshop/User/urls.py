from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup',views.signup , name="signup"),
    path("login/" , views.loginwithemail , name="login"),
    path("logout/",views.userlogout , name="logout"),
    path("forgetpassword/" , views.forgetpassword , name="forgetpassword"),
    path("changepassword/" , views.changepassword , name="changepassword"),
    path("address/" , views.addaddress , name="address"),
    path("deleteaddress/<int:id>/" , views.del_address , name="del-address"),
    path("profile/" , views.profile , name="profile"),
    path("editprofile/", views.edit_profile , name="edit-profile")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
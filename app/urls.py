from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_views,register_views,request_page_views,view_details



urlpatterns = [
   path('',home_views,name="home"),
   path('register/',register_views,name="register"),
   path('request/',request_page_views,name="request"),
   path('request/viewdetails/<int:id>/',view_details,name="viewdetails"),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_views,register_marriage_views,request_page_views,view_details,image_views,admin_approve_views,admin_reject_view,register,login,logout,marriageCertifficate,help_views,terms_condition_views,data_protection_view,disclaimer_view,privacy_view,contactus_views



urlpatterns = [
   path('',home_views,name="home"),
   path('register/',register,name="register"),
   path('login/',login,name="login"),
   path('logout/',logout,name="logout"),
   
   
   path('register_marriage_views/',register_marriage_views,name="marriageregister"),
   path('request/',request_page_views,name="request"),
   path('request/viewdetails/<int:id>/',view_details,name="viewdetails"),
   
   
   path('image/',image_views,name="image"),
   path('request/admin_approve_views/<int:id>/',admin_approve_views,name="approve"),
   path('request/admin_reject_view/<int:id>/',admin_reject_view,name="reject"),
   
   path('request/admin_reject_view/<int:id>/',admin_reject_view,name="reject"),
   path('marriageCertifficate/<int:id>/',marriageCertifficate,name="certificate"),
   path('help/',help_views,name="help"),
   
   
   path('terms_condition_views/',terms_condition_views,name="terms"),
   path('data_protection_view/',data_protection_view,name="dataprotection"),
   path('disclaimer_view/',disclaimer_view,name="disclaimer"),
   path('privacy_view/',privacy_view,name="privacy"),

   path('contactus_views/',contactus_views,name="contactus")
   
   

   


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
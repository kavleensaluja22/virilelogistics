from appname import views 
from django.urls import path, include
from  django.conf.urls.static import settings , static#new
urlpatterns = [
 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('base', views.base, name='base'),
    path('contact', views.contact_view, name='contact'),
    path('service', views.service, name='service'),
    path('submit-contact-form/', views.submit_contact_form, name='submit_contact_form'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
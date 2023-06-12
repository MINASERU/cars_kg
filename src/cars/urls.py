from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories,  name='categories'),
    path('vehicle/', views.vehicles, name = 'vehicles'),
    path('vehicle/<int:pk>', views.VehicleDetailView.as_view(), name='vehicle-details')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
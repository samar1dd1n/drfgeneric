from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
    path('gv/', include('car.urls')),
    path('cbv_gav/', include('car.urls'))
]
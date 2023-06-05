from django.contrib import admin
from django.urls import path,include
from India import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('absamajhrahahaibharat/', include(("India.urls","map"), namespace="map")),
    path('community/',include(("community.urls", "community"), namespace="community")),
    path('', views.index, name="index")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

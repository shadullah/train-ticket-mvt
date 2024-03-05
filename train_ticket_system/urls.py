
from django.contrib import admin
from django.urls import path,include
from core.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('account.urls')),
    path('train/', include('train.urls')),
    path('<slug:station_slug>', HomeView.as_view(),name='station_wise'),
]

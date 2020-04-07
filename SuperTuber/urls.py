from django.contrib import admin
from django.urls import path
from FindTutors import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('home/', include('FindTutors.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    path('', views.SignUpView.as_view(), name='signup'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('complete/google-oauth2/home/',views.redirectView.as_view(), name='redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




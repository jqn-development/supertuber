from django.urls import path
from django.conf.urls import url

from . import views
from SuperTuber import settings
from django.conf.urls.static import static

app_name = 'FindTutors'

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='signup'),
    path('tutors/', views.Tutors, name='tutors'),
    path('tutees/', views.Tutees, name='tutees'),
    path('request/', views.RequestView.as_view(), name='request'),
    path('register_tutor/', views.TutorRegister.as_view(), name='tutor_register'),
    path('register_tutee/', views.TuteeRegisterView.as_view(), name='tutee_register'),
    path('request/tutor_request/', views.TutorRequest, name='tutor_request'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.editprofile, name='edit_profile'),
    path('request/tutor_request/', views.TutorRequest, name='tutor_request'),
    path('tutors/<pk>/', views.TutorProfile, name='tutor_profile'),
    path('ratingsreview/', views.ReviewRating, name='ratings_review'),
    url(r'messages/$', views.all_rooms, name="all_rooms"),
    url(r'token$', views.token, name="token"),
    url(r'(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

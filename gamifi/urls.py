from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import AerobicCreateView, AerobicUpdateView, ExerciseDetailView,StrengthCreateView, StrengthUpdateView, FlexibilityCreateView,FlexibilityUpdateView

app_name = 'gamifi'

urlpatterns = [
    path("", views.home, name="home"),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),
    path('profile/', views.profile,name="profile"),
    path('editprofile/', views.edit_profile,name="edit-profile"),
    path('exercise/Aerobic/new/', AerobicCreateView.as_view(), name='aerobic-create'),
    path('exercise/Strength/new/', StrengthCreateView.as_view(), name='strength-create'),
    path('exercise/Flexibility/new/', FlexibilityCreateView.as_view(), name='flexibility-create'),
    path('exercise/Aerobic/update/<int:pk>', AerobicUpdateView.as_view(), name='aerobic-update'),
    path('exercise/Strength/update/<int:pk>', StrengthUpdateView.as_view(), name='strength-update'),
    path('exercise/Flexibility/update/<int:pk>', FlexibilityUpdateView.as_view(), name='flexibility-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
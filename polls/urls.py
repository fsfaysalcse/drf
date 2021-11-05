from django.urls import path
from .views import PollAPIView

urlpatterns = [
   path('poll/', PollAPIView.as_view()),
]


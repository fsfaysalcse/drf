from django.urls import path
from .views import PollAPIView, PollDetailsUpdateDeleteView

urlpatterns = [
   path('poll/', PollAPIView.as_view()),
   path('poll/delete/<pk>/', PollDetailsUpdateDeleteView.as_view()),
]

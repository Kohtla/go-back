from django.contrib import admin
from django.urls import path, include

from votes.views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('votes', include('votes.urls', namespace='votes')),
    path('users', UserView.as_view(), name='user_view')
]

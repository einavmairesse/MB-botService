from django.urls import path, include

urlpatterns = [
    path('', include('bot_app.urls')),
    path('test/', include('bot_app.urls'))
]
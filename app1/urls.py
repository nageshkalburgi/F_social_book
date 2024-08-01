# users/urls.py
from django.urls import path
from .views import dashboard, register, login
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import send_test_email


urlpatterns = [
    path('home/', dashboard, name='home'),
    path('register/', register, name='register'),
    path('', login, name='login'),
    path("logout/",views.custom_logout , name="logout"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('password_reset',views.password_reset,name='password_reset'),

    path('authors-and-sellers/', views.authors_and_sellers, name='authors_and_sellers'),
    path('upload/', views.upload_file, name='upload_file'),
    path('uploaded-files/', views.uploaded_files, name='uploaded_files'),
    path('send-email/', send_test_email, name='send_test_email'),
    # path('api/users/', views.UserListCreateView.as_view(), name='user-list-create'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from Activity import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Login and Logout
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", views.logout, name='logout'),
    
    # User Registration
    path('register/', views.register, name='register'),
    
    # User Profile and other pages
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('subscription/', views.subscription, name="subscription"),
    path('contact/', views.contact, name="contact"),
    path('songs/', views.songs, name="songs"),

    path('spotify/dashboard/', views.spotify_dashboard,name='spotify_dashboard'),
    path('spotifylogin/',views.spotify_login,name='spotify_login'),
    path('spotify/callback/', views.spotify_callback, name='spotify_callback'),

    path('update_profile/', views.update_profile, name='update_profile'),
      path('search/', views.search, name='search'),  # Handles search functionality
    path('category/', views.category, name='category'),
    path('notifications/', views.notifications, name='notifications'),
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#from django.urls import path
#from . import views

#urlpatterns = [
    # other URL patterns
    #path('update_profile/', views.update_profile, name='update_profile'),
#]

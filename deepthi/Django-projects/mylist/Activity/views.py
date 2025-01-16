from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import  CreateUserForm
from django.contrib.auth.models  import User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from django.contrib.auth.decorators import login_required


from django.shortcuts import redirect
from urllib.parse import urlencode
import secrets

def spotify_login(request):
    state = secrets.token_hex(16)
    request.session['spotify_auth_state'] = state
    
    params = {
        'response_type': 'code',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'scope': 'user-read-private user-read-email',
        'redirect_uri': settings.SPOTIFY_REDIRECT_URI,
        'state': state
    }
    
    auth_url = f'https://accounts.spotify.com/authorize?{urlencode(params)}'
    return redirect(auth_url)


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.save()
            messages.success(request,'Your Account has Been Created')
            return redirect('login')
        else:
            messages.warning(request,'password mismathching !!!')
            return redirect('register')
    else:
        form=CreateUserForm()
        return render(request,'register.html',{'form':form})
def logout(request):
    auth_logout(request)
    return render(request,'logout.html')
@login_required    
def profile(request):
    return render(request,'profile.html')
def about(request):
    return render(request,'about.html')
@login_required  
def subscription(request):
    return render(request,'subscription.html')
def contact(request):
    return render(request,'contact.html')
def songs(request):
    return render(request,'songs.html')



def spotify_dashboard(request):
    """Displays a simple Spotify dashboard."""
    access_token = request.session.get('spotify_access_token')
    if not access_token:
        return redirect('spotify_login')

    # Fetch user's Spotify data
    user_profile_url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_response = requests.get(user_profile_url, headers=headers)
    user_data = user_response.json()

    redirect_url = f"https://open.spotify.com?access_token={access_token}"
    return HttpResponseRedirect(redirect_url)


def spotify_login(request):
    """Redirects to Spotify for user authorization."""
    scope = "user-read-private user-read-email"  # Add scopes as required
    auth_url = (
        "https://accounts.spotify.com/authorize?"
        f"client_id={settings.SPOTIFY_CLIENT_ID}&response_type=code"
        f"&redirect_uri={settings.SPOTIFY_REDIRECT_URI}"
        f"&scope={scope}"
    )
    return redirect(auth_url)

def spotify_callback(request):
    """Handles Spotify callback and fetches an access token."""
    code = request.GET.get('code')
    if not code:
        return render(request, 'error.html', {"message": "Authorization failed."})

    # Exchange the authorization code for an access token
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "client_secret": settings.SPOTIFY_CLIENT_SECRET,
    }
    response = requests.post(token_url, data=payload)
    response_data = response.json()

    access_token = response_data.get('access_token')
    if not access_token:
        return render(request, 'error.html', {"message": "Failed to get access token."})
    print(access_token)
    # Save the access token in the session
    request.session['spotify_access_token'] = access_token
    return redirect('spotify_dashboard')  # Redirect to a page to browse Spotify contentfrom django.shortcuts import render

    
#from django.shortcuts import render

def update_profile(request):
    # logic for updating the profile
    return render(request, 'profile_update.html',{'request':request})


#from django.shortcuts import render

#def your_view(request):
    # Pass request to template
    #return render(request, 'your_template.html', {'request': request})




from django.shortcuts import render
from .forms import SearchForm
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Setup Spotify authentication
def get_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(client_id='3822ebda03344da681e15f1f382eb1d0', client_secret='')
    sp = Spotify(client_credentials_manager=client_credentials_manager)
    return sp

# Create a view for the search results
def search(request):
    """Handles searching for songs and artists from Spotify."""
    results = None
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            
            # Retrieve the access token from session
            access_token = request.session.get('spotify_access_token')
            if not access_token:
                return redirect('spotify_login')  # If there's no access token, redirect to login

            # Use the access token to authenticate the Spotify API
            sp = spotipy.Spotify(auth=access_token)

            # Search Spotify for songs and artists
            try:
                results = sp.search(q=query, limit=10)  # Adjust the limit as needed
            except spotipy.exceptions.SpotifyException as e:
                return render(request, 'error.html', {"message": f"Error: {str(e)}"})
    else:
        form = SearchForm()

    return render(request, 'search_results.html', {'form': form, 'results': results})


def category(request):
    return render(request, 'category.html')

def notifications(request):
    return render(request, 'notifications.html')

    
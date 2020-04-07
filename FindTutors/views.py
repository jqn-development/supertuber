from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .models import Request, TUser, Reviews, Room
from .forms import RequestForm, RegisterForm, ProfileUpdateForm, TutorRegistration, TutorUserSignUpForm, \
    ReviewRatingForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

# tutor register form view


class TutorRegister(CreateView):
    model = TUser
    form_class = TutorUserSignUpForm
    template_name = 'FindTutors/tutor_signup.html'  # correct form HTML

    def form_valid(self, form):

        user = form.save(commit=False)
        user.is_tutor = True
        user.save()
        return redirect('/home/tutors/')  # Go back to the table of tutors


class TuteeRegisterView(CreateView):
    model = TUser
    # form_class = RegisterForm               # check form
    fields = ['firstname', 'lastname', 'email', 'subjects', 'year', ]
    template_name = 'FindTutors/tutee_signup.html'  # correct form HTML

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_tutee = True
        user.save()
        return redirect('/home/tutees/')  # Go back to the table of tutors
        login(self.request, user)

        return redirect('dashboard')           # redirect to proper dashboard


def Tutors(request):
    model = TUser
    # the_tutors = []
    the_tutors = TUser.objects.filter(is_tutor=1)
    # the_tutors = TUser.objects.all()
    return render(request, 'FindTutors/tutors.html', {'tutors': the_tutors})


def TutorProfile(request, pk):
    if request.method == 'GET':
        profile = get_object_or_404(TUser, pk=pk)  # change to TutorProfile
        profile_id = pk
        reviews = Reviews.objects.filter(profile_id=profile_id)

        return render(request, 'FindTutors/tutor_profile.html', {'profile': profile, "reviews": reviews})


def Tutees(request):
    all_tutees = TUser.objects.filter(is_tutee=True)
    return render(request, 'FindTutors/tutees.html', {'tutees': all_tutees})

# registration views


class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'


class redirectView(generic.TemplateView):
    template_name = 'registration/redirect.html'


class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'


class RequestView(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'FindTutors/request.html'

    def form_valid(self, form):
        self.request_input = form.save(commit=False)
        self.request_input.sender = self.request.user
        self.request_input.recipient = TUser.objects.get(
            email=self.request.GET.get('recipient'))
        self.request_input.save()
        return redirect('/home/request/tutor_request/')


def TutorRequest(request):
    model = TUser
    all_tutors = TUser.objects.filter(is_tutor=True)
    if request.user.is_authenticated:
        print('pie')
    return render(request, 'FindTutors/tutor_request.html', {'tutors': all_tutors})


class ProfileView(generic.TemplateView):
    template_name = 'FindTutors/myprofile.html'


@login_required
def editprofile(request):
    if request.method == 'POST':
        print("--- request ----")
        print(request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('FindTutors:profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'FindTutors/editprofile.html', context)


def ReviewRating(request):
    if request.method == "POST":
        form = ReviewRatingForm(request.POST)
        if form.is_valid():
            rating = form.save()
            return redirect('/home/tutors/%s' % rating.profile_id)
    else:
        form = ReviewRatingForm()
    return render(request, 'FindTutors/ratings_review.html', {'form': form})


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'FindTutors/all_rooms.html', {'rooms': rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'FindTutors/room_detail.html', {'room': room})


fake = Faker()


def token(request):
    identity = request.GET.get('identity', fake.user_name())
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Quiz, Question, Answer, UserAnswer, UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .forms import EditProfileForm
# Create your views here.
def index(request):
    users = UserProfile.objects.all().order_by('-score')[:3]
    return render(request, 'index.html', {'users' : users})

def done(request):
    return render(request, 'done.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'formulario': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                usuario = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user_profile = UserProfile.objects.create(user = usuario)
                usuario.save()
                user_profile.save()
                login(request, usuario)
                return redirect('home')
            except:
                return render(request, 'signup.html', {'formulario': UserCreationForm, 'mensaje':'Este usuario ya existe'})
        return render(request, 'signup.html', {'formulario': UserCreationForm})

def closelog(request):
    logout(request)
    return redirect('index')

def logger(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': AuthenticationForm(), 'mensaje': 'Usuario y/o contraseña incorrecto'})
        except MultiValueDictKeyError:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'mensaje': 'Falta información de inicio de sesión'})

@login_required
def home(request):
    quest = Quiz.objects.all()
    return render(request, 'home.html',{'username':request.user, 'quest':quest})

def show_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz = quiz)
    pos_answers = {}
    for question in questions:
        answer = question.answer_set.all()
        pos_answers[question] = answer
    return render(request, 'show_quiz.html', {'quiz': quiz, 'pos_answers':pos_answers})

@login_required
def answer_process(request):
    user = request.user
    if request.method == 'POST':
        for question, answers in request.POST.items():
            if question.startswith('respuesta_'):
                question_id = int(question.split('_')[1])
                selected_answer_id = int(answers)
                respuesta_seleccionada = Answer.objects.get(id=selected_answer_id)
                # Guardar la respuesta seleccionada por el usuario o realizar cualquier otra acción necesaria
                user_answer = UserAnswer.objects.create(
                    user=user,
                    question_id=question_id,
                    answer_id=selected_answer_id
                )
                if respuesta_seleccionada.is_correct:
                    # Si la respuesta es correcta, incrementar el puntaje del usuario
                    user_profile = UserProfile.objects.get(user=user)
                    user_profile.score += 1
                    user_profile.save()
    else:
        return redirect('show_quiz')
    return redirect('done')

def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'profile.html', {'form': form, 'mensaje': 'error al actualizar datos'})
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form, 'user' : request.user})
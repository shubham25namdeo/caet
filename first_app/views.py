from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from .workday import *
from .forms import *
from .models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib
import datetime
import random
from django.utils import timezone
from reportlab.pdfgen import canvas
from django.utils.html import strip_tags


all_users_list = []
user_list_print = []
final_print_online_list = []


def register_confirm(request, activation_key):
    # check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home/')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    # check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('/accounts/login/')
    # if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('registration/confirm.html')


def register_user(request):
    args = {}

    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form

        if form.is_valid():
            form.save()  # save user to database if form is valid
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1((str(random.random())).encode('utf8')).hexdigest()[:5]
            activation_key = hashlib.sha1((salt + email).encode('utf8')).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            print(activation_key, "activation key")
            # Get user by username
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            # Create and save user profile
            new_profile = UserProfile(user=user, activation_key=activation_key,
                                      key_expires=key_expires)
            new_profile.save()

            # Send email with activation key
            email_subject = 'Account confirmation'
            print(email_subject)
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48 hours http://127.0.0.1:8000/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'shubham.namdeo@gmail.com',
                      [email], fail_silently=False)

            return HttpResponseRedirect('/success/')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('registration/register.html', args, context_instance=RequestContext(request))


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    a = request.user.id
    logout(request)
    all_users_list.remove(str(a))
    return HttpResponseRedirect('/')


@login_required
def home(request):
    for i in request.session.keys():
        print(request.session[i])
        print(i)
        if request.session['_auth_user_id'] not in all_users_list:
            all_users_list.append(request.session['_auth_user_id'])

    print(all_users_list, "trial run")
    return render_to_response(
        'home.html',
        {'user': request.user}
    )


@login_required
def team(request):
    return render_to_response(
        'Team.html',
        {'user': request.user}
    )


@login_required
def vid(request):
    print("hi vid")
    return render_to_response(
        'home.html',
        {'user': request.user}
    )


@login_required
def newnotes(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = Note.objects.create()
        form.title = request.POST.get('title')
        form.notes = request.POST.get('notes')
        form.logged_user = str(request.user)
        form.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
        form.save()
        user_loggedin = str(request.user)
        my_data = Note.objects.all().filter(logged_user=user_loggedin)
        return render_to_response('notes.html', {'user_loggedin': user_loggedin, 'my_data': my_data},
                                  context_instance=RequestContext(request))
    else:
        user_loggedin = str(request.user)
        my_data = Note.objects.all().filter(logged_user=user_loggedin)
        return render_to_response('notes.html', {'user_loggedin': user_loggedin, 'my_data': my_data},
                                  context_instance=RequestContext(request))


@login_required
def chats(request):
    args = {}

    args.update(csrf(request))
    if request.method == 'POST':
        form = CommentForm(request.POST.get('commentform'))
        form.comment = request.POST.get('comments')
        form.logged_inuser = request.user
        form.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
        form.save()
        lists = []
        for i in CommentForm.objects.all():
            print(i.comment)
            lists.append(i.comment)
        my_data = CommentForm.objects.filter().order_by('-id')
        my_users = UserProfile.objects.all()
        user_loggedin = request.user

        return render_to_response('chat.html', {'user_loggedin': user_loggedin, 'all_user_list': all_users_list,
                                                'com': lists[-1], 'my_data': my_data, 'my_users': my_users,
                                                'user_list_print': final_print_online_list},
                                  context_instance=RequestContext(request))

    else:
        user_loggedin = request.user
        my_data = CommentForm.objects.filter().order_by('-id')
        my_users = User.objects.all()
        for i in user_list_print:
            if i not in final_print_online_list:
                final_print_online_list.append(i)

        for i in all_users_list:
                print(i, "sadklsadhjkjadnhaksd")
                username_all = User.objects.get(id=i)
                print(username_all.first_name, "qweqweqweqweqweqweqwe")
                user_list_print.append(username_all.first_name)

        return render_to_response('chat.html',
                                  {'user_loggedin': user_loggedin, 'all_user_list': all_users_list,
                                   'my_data': my_data, 'my_users': my_users,
                                   'user_list_print': final_print_online_list},
                                  context_instance=RequestContext(request))


@login_required
def articles(request):
        args = {}

        args.update(csrf(request))
        if request.method == 'POST':
            form = ArtForm(request.POST, request.FILES)
            if form.is_valid():
                form.title = request.POST.get('title')
                form.desc = request.POST.get('description')
                form.docfile = Art(docfile=request.FILES['docfile'])
                form.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
                form.save()

                my_data = Art.objects.all()
                user_loggedin = str(request.user)

                return render_to_response('articles.html', {'form': form, 'my_data': my_data,
                                                            'user_loggedin': user_loggedin},
                                          context_instance=RequestContext(request))

        else:
            user_loggedin = str(request.user)
            print(len(all_users_list))

            my_data = Art.objects.all()
            form = ArtForm()

            return render_to_response('articles.html', {'form': form, 'my_data': my_data,
                                                        'user_loggedin': user_loggedin},
                                      context_instance=RequestContext(request))


@login_required
def docs(request):
    args = {}

    args.update(csrf(request))
    if request.method == 'POST':
        lists = Word.objects.create()
        lists.texts = request.POST.get('editor1')
        lists.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
        lists.save()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="new_pdf.pdf"'
        p = canvas.Canvas(response)
        filtered = strip_tags(lists.texts)[:-2]
        p.drawString(100, 750, filtered)
        p.showPage()
        p.save()
        return response

    else:
        comm = Word.objects.all()
        form = WordForm()
        return render_to_response('docx.html', {"comm": comm, "form": form}, context_instance=RequestContext(request))


@login_required
def add_consultant(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = ConsultantForm(request.POST, request.FILES)
        if form.is_valid():
            form.cname = request.POST.get('cname')
            form.projtype = request.POST.get('projtype')
            form.location = request.POST.get('location')
            form.joindate = request.POST.get('datepicker')
            form.resume = Consultant(resume=request.FILES['resume'])
            form.JD = request.POST.get('JD')
            form.log_user = request.user
            form.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
            print(form.log_user, "a!!!!!!!!!!!!!!!!!")
            form.save()
            user_loggedin = str(request.user)
            my_data = Consultant.objects.all().filter(log_user=user_loggedin)
            return render_to_response('addconsultant.html', {'user_loggedin': user_loggedin, 'my_data': my_data,
                                                             'form': form},
                                      context_instance=RequestContext(request))

    else:
        user_loggedin = str(request.user)
        my_data = Consultant.objects.all()
        form = ConsultantForm()
        return render_to_response('addconsultant.html', {'user_loggedin': user_loggedin, 'my_data': my_data,
                                                         'form': form},
                                  context_instance=RequestContext(request))


@login_required
def view_consultant(request):
    user_loggedin = request.user
    my_data = Consultant.objects.all().filter(log_user=user_loggedin)
    my_task = Task.objects.all().filter(log_user=user_loggedin)
    my_ctask = Task.objects.all()
    cd = datetime.date.today()
    holidays = [datetime.date(2016, 5, 2), datetime.date(2016, 5, 3)]
    workingDays = networkdays(datetime.date(2016, 1, 1), datetime.date(2016, 12, 31), holidays)
    print(type(workingDays), workingDays)
    from datetime import date, timedelta
    for i in my_data:
        timedelta_t = date.today() - i.joindate
        print(timedelta_t)
    args = {}
    args.update(csrf(request))
    for i in my_data:
        print(i.cname)
        print(i.id, "is id for consultant ", i.cname)
        print(all_users_list, "trial trial")

    if request.method == 'POST':
        lists = Task.objects.create()
        lists.title = request.POST.get('Title')
        lists.cname = request.POST.get('cname')
        lists.desc = request.POST.get('Desc')
        lists.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
        lists.log_user = str(request.user)
        print(lists.title)
        lists.save()

        return render_to_response('veiwconsultants.html', {'my_data': my_data, 'WorkingDays': workingDays,
                                                           'cd': cd, 'my_task': my_task, 'my_ctask': my_ctask,
                                                           'timedelta': timedelta},
                                  context_instance=RequestContext(request))

    return render_to_response('veiwconsultants.html', {'user_loggedin': user_loggedin, 'WorkingDays': workingDays,
                                                       'my_data': my_data, 'cd': cd, 'my_task': my_task,
                                                       'my_ctask': my_ctask, 'timedelta': timedelta},
                              context_instance=RequestContext(request))


@login_required
def edit_consultant(request, ids=8):
    instance = get_object_or_404(Consultant, id=ids)
    args = {}
    args.update(csrf(request))
    form = ConsultantForm(request.POST or None, request.FILES, instance=instance)
    print(form, "form")
    if form.is_valid():
        print("here here here here here here here here")
        form.cname = request.POST.get('cname')
        form.projtype = request.POST.get('projtype')
        form.location = request.POST.get('location')
        form.joindate = request.POST.get('datepicker')
        form.resume = Consultant(resume=request.FILES['resume'], default=None)
        form.JD = request.POST.get('JD')
        form.log_user = request.user
        form.dates = datetime.datetime.utcnow().replace(tzinfo=utc)
        print(form.log_user, "a!!!!!!!!!!!!!!!!!")
        form.save()
        user_loggedin = str(request.user)
        my_data = Consultant.objects.all().filter(log_user=user_loggedin)
        return render_to_response('home_back.html', {'user_loggedin': user_loggedin, 'my_data':my_data, 'form': form},
                                  context_instance=RequestContext(request))

    user_loggedin = str(request.user)
    my_data = Consultant.objects.filter(id=8)
    return render_to_response('editconsultant.html', {'my_data': my_data, 'user_loggedin': user_loggedin, 'form': form},
                              context_instance=RequestContext(request))


from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import*
import string
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    return render(request, 'client_resources/welcome.html')


def index(request):
    new_user = User.objects.get(id=request.session['user_id'])
    context = {
      #'all_clients': Client.objects.all()
      'all_clients': new_user.new_clients.all(),
      'new_user':new_user
    }
    return render(request,'client_resources/index.html',context)

def update_proj_note(request,id):
    if request.method != 'POST':
        print "post faild"
        return redirect(reverse('edit_proj_note', kwargs={'id' : id}))
    else:
        #user = User.objects.get(id=request.session['user_id'])
        print "just in update proj note"
        note = Project.objects.update(request.POST)
        if note[0] == False:
            for error in note[1]:
                messages.error(request,error)
                print "update error"
            return redirect(reverse('edit_proj_note', kwargs={'id':id}))
        else:
            #user = User.objects.get(id=request.session['user_id'])
            print "in update proj note"
            print id
            proj_update = Project.objects.get(id=id)

            proj_update.project_notes = request.POST.get('notes')
            print proj_update.project_notes

            proj_update.save()
            return redirect(reverse('show_project', kwargs={'id':id}))


def edit_proj_note(request,id):
    project = Project.objects.get(id=id)
    print "got to edit_proj_note"
    context = {
    'project':project
    }
    return render(request,'client_resources/ProjectNote.html',context)
def remove_project(request,id):
    project = Project.objects.get(id=id)
    print project.id
    print "got to project delete"
    print project.client.id
    project.delete()
    return redirect(reverse('show_page', kwargs={'id':project.client.id}))
def remove(request,id):
    client = Client.objects.get(id=id)
    print "got to delete"
    client.delete()
    return redirect(reverse('my_index'))


def edit(request,id):
    client = Client.objects.get(id=id)
    print "got to edit"
    context = {
     'client':client
    }
    return render(request,'client_resources/edit.html',context)

def update(request,id):
    if request.method != 'POST':
        print "post faild"
        return redirect(reverse('edit', kwargs={'id' : id}))
    else:
        #user = User.objects.get(id=request.session['user_id'])
        print "just in update"
        client = Client.objects.addClient(request.POST)
        if client[0] == False:
            for error in client[1]:
                messages.error(request,error)
                print "update error"
            return redirect(reverse('edit', kwargs={'id':id}))
        else:
            #user = User.objects.get(id=request.session['user_id'])
            print "in update client"
            #print user.id
            client_update = Client.objects.get(id=id)
            client_update.name = request.POST.get('name')
            client_update.email = request.POST.get('email')
            client_update.phone = request.POST.get('phone')
            client_update.notes = request.POST.get('notes')

            client_update.save()
            return redirect(reverse('my_index'))


def new(request):
    return render(request, 'client_resources/new.html')

def create(request):
    if request.method != 'POST':
        return redirect(reverse('new'))
    else:
        client = Client.objects.addClient(request.POST)
        if client[0] == False:
            for error in client[1]:
                messages.error(request,error)
            return redirect(reverse('new'))
        else:
            user = User.objects.get(id=request.session['user_id'])
            print "in add client"

            new_client = Client.objects.create(
               name = request.POST.get('name'),
               email = request.POST.get('email'),
               phone = request.POST.get('phone'),
               notes = request.POST.get('notes'),
               new_user = user

            )
            request.session['client_id'] = new_client.id

        #client = Client.objects.create(name=request.POST['name'],email=request.POST['email']
        # , phone=request.POST['phone'],notes=request.POST['notes'])
        #new_client = Client.objects.get(id=client.id)
        #request.session['client_id'] = new_client.id
        context = {
          'client':new_client,
          'client_name':string.capwords(new_client.name)
        }
        return render(request, 'client_resources/display.html',context)


def show(request,id):
    disp_client = Client.objects.get(id=id)
    print "got to show"
    print disp_client.name
    context = {
      'client':disp_client,
      'client_name':string.capwords(disp_client.name)
    }
    return render(request,'client_resources/display.html',context)

def add_project(request,id):
    #print "Project created"
        #print client_project.name
        #context = {
         #'client':client,
        # 'projects':client.projects.all(),
         #'client_project_name':string.capwords(client_project.name)
        #}
        #return render(request,'client_resources/projshow.html',context)

    client = Client.objects.get(id=id)
    if request.method != 'POST':
        print "add project no post"
        return redirect(reverse('project_page', kwargs={'id': id}))
    else:
        project = Project.objects.addProject(request.POST)
        if project[0] == False:
            for error in project[1]:
                messages.error(request,error)
                print "got to error"
            return redirect(reverse('project_page', kwargs={'id': id}))
        else:

            print "in add project"

            new_project = Project.objects.create(
               name = request.POST.get('name'),
               project_notes = request.POST.get('notes'),
               client = client
            )

            client_project = new_project.id
            print "Project created"
            print client_project
            request.session['client_id'] = client.id

        context = {
          'client':client,
          'client_project':new_project,#client_project,
          'projects':client.projects.all(),
        }
        return render(request,'client_resources/projshow.html',context)


def project_page(request,id):
    client = Client.objects.get(id=id)
    context = {
    'client': client
    }
    return render(request,'client_resources/addproject.html',context)
    
def proj_show(request,id):
    client_project = Project.objects.get(id=id)
    print client_project.client.id
    print client_project.id
    print "in project show"
    print string.capwords(client_project.name)
    print client_project.project_notes
    client_project.project_notes = client_project.project_notes
    context = {
      'client_project':client_project,
      'client':client_project.client,
      'client_project_name':string.capwords(client_project.name)

    }
    return render(request,'client_resources/projshow.html',context)
def main(request):
    return render(request, 'client_resources/main.html')



def login(request):
    if request.method != 'POST':
        return redirect('/main')
    else:
        if request.POST.get('email') == '' or request.POST.get('password') == '':
            messages.error(request, 'invalid credentials')
            return redirect('/main')
        check = User.objects.loginUser(request.POST)
        if check['status'] == False:
            messages.error(request, check['message'])
            return redirect('/main')
        else:
            request.session['user_id'] = check['user'].id
            return redirect('/index')

def createUser(request):
	if request.method != 'POST':
		return redirect(reverse('main'))
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request, error)
			return redirect(reverse('main'))
		else:
			#create the user
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				password = hashed_pw
			)
			request.session['user_id'] = user.id
			return redirect('/index')
def logout(request):
    request.session.clear()
    return redirect(reverse('welcome'))


def back(request):
    return redirect(reverse('show_page'))

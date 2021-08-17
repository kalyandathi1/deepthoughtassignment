#2. To-Do App 
#A to-do app is a software application that lets you make a list of tasks that you need to complete. You can make daily or weekly lists of tasks in a to-do app. Once you complete a task, you can mark it “completed” and update your to-do list. It is a convenient app that lets you keep track of your chores.
#To build a to-do app, you need not be a proficient Django developer – you only need to have good knowledge of Django basics. You can create a simple to-do app using tools like JavaScript, HTML, and CSS, and then host your app on the localhost server by using Django/Flask framework.

#Modules required : 
#django : install django
#crispy_forms : 
#pip install --upgrade django-crispy-forms
#basic setup :
#Start a project by the following command – 
 
#django-admin startproject todo-site
#Change directory to todo-site – 
 
#cd todo-site
#Start the server- Start the server by typing following command in terminal – 

#python manage.py runserver
#To check whether the server is running or not go to a web browser and enter http://127.0.0.1:8000/ as URL.
#Now stop the server by pressing 

#ctrl-c
#Let’s create an app now.
 

#python manage.py startapp todo
#Goto todo/ folder by doing : cd todo and create a folder with index.html file : templates/todo/index.html
#Open the project folder using a text editor. The directory structure should look like this :
  
  
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
	#####################home_page###########################################
	path('', views.index, name="todo"),
	####################give id no. item_id name or item_id=i.id ############
	path('del/', views.remove, name="del"),
	########################################################################
	path('admin/', admin.site.urls),
]

##Edit models.py in todo : 

from django.db import models
from django.utils import timezone

class Todo(models.Model):
	title=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title</pre>

#Edit views.py in todo :

from django.shortcuts import render, redirect
from django.contrib import messages

## import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################

def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = TodoForm()

	page = {
			"forms" : form,
			"list" : item_list,
			"title" : "TODO LIST",
		}
	return render(request, 'todo/index.html', page)



### function to remove item, it receive todo item id from url ##
def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')


#Now create a forms.py in todo : 

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields="__all__"</pre>

#Navigate to templates/todo/index.html and edit it 
'''Make migrations and migrate it 

 

python manage.py makemigrations
python manage.py migrate
Now you can run the server to see your todo app 
 

python manage.py runserver...

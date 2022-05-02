from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import EntryForm, TopicForm

from .models import Entry, Topic
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics}

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()
    context = {'topic':topic,'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)#only field showing up on the entry field is TEXT
            #entry model has 3 fields: topic, text, date added
            #commit writes to the database
            #commit is set to false so it won't wwrite because we need to do something else 
            new_entry.topic = topic #line 45 is how we are getting the topic
            new_entry.save()
            return redirect('MainApp:topic',topic_id=topic_id)#we don't use line 39 topic because it is 
            #a whole object, and topic_id is simply an integer
    context = {"form": form, 'topic':topic}
    return render(request, "MainApp/new_entry.html", context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic #lowercase entry beause this is the variable that is storing the particular object 
    
    if request.method != 'POST':
        form = EntryForm(instance=entry) #equal to the object we have the id for. this is wehre the existing data will be loaded 
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)
    
    context = {"form": form, "topic": topic, 'entry':entry}
    return render(request, "MainApp/edit_entry.html", context)
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# function (def) called post_list that takes a request and will return the value it gets from calling another function - render - that will render (put together) our template blog/post_list.html.

#We have different pieces in place: the Post model is defined in models.py, we have post_list in views.py and the template added. But how will we actually make our posts appear in our HTML template? Because that is what we want to do – take some content (models saved in the database) and display it nicely in our template, right?

#This is exactly what views are supposed to do: connect models and templates. In our post_list view we will need to take the models we want to display and pass them to the template. In a view we decide what (model) will be displayed in a template.

# Remember when we talked about including code written in different files? Now is the moment when we have to include the model we have written in models.py. We will add the line from .models import Post like this:

# blog/views.py

# from django.shortcuts import render
# from .models import Post

# The dot before models means current directory or current application. Both views.py and models.py are in the same directory. This means we can use . and the name of the file (without .py). Then we import the name of the model (Post).

# To take actual blog posts from the Post model we need something called QuerySet... So, let's open the blog/views.py file in the code editor, and add this piece of code to the function def post_list(request) -- but don't forget to first add from django.utils import timezone..

# To display our QuerySet on our blog's post list, we have two things left to do:

#     Pass the posts QuerySet to the template context, by changing the render function call. We'll do this now.
#     Modify the template to display the posts QuerySet.
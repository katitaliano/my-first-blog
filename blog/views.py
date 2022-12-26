from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# function (def) called post_list that takes a request and will return the value it gets from calling another function - render - that will render (put together) our template blog/post_list.html.
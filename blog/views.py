from django.shortcuts import render

# Create view

def post_list(request):
    return render(request, 'blog/post_list.html', {})

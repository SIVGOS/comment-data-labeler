from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib import messages
import random
from .models import Comment

def home(request):
    return redirect('/labeler')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        print(user)
        if not user:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
        auth.login(request, user)
        return redirect('/labeler')

@login_required(login_url='/login')
def logout_method(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def labeler_method(request):
    if request.method == 'GET':
        print(request.path)
        comments = Comment.objects.filter(tags__isnull=True)
        available_comments = len(comments)
        comment = comments.first()
        labelled_comments = Comment.objects.filter(tags__isnull=False).count()
        return render(request, 'labeler_firm.html', {'comment_text': comment.comment_text, 'comment_id': comment.comment_id,
            'video_title': comment.video_title, 'available_comments': available_comments, 'labelled_comments': labelled_comments})
    if request.method == 'POST':
        tags = []
        for f in ["timestamp", "thanks", "greetings", "question", "doubt", "suggestion", "future-question", "disagree", "other", "non-english"]:
            if f in request.POST.keys():
                tags.append(f)
        if not tags:
            return redirect('/labeler')
        
        comment_id = request.POST.get('comment_id')
        tags = '+'.join(tags)
        comment = Comment.objects.filter(comment_id=comment_id).first()
        comment.tags = tags
        comment.save()
        return redirect('/labeler')

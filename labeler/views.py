from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Comment, Labels, LabellerMap
from .helper import format_label_name

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
    labels = Labels.objects.all()
    if request.method == 'GET':
        tagged_by_user = LabellerMap.objects.filter(user=request.user).values_list('comment_id', flat=True)
        available_comments = Comment.objects.count()
        comments = Comment.objects.exclude(id__in = tagged_by_user)
        labelled_comments = comments.count()
        comment = comments.first()
        context = {'comment_text': comment.comment_text,
                    'comment_id': comment.comment_id,
                    'labels': labels,
                    'video_title': comment.video_title,
                    'available_comments': available_comments,
                    'labelled_comments': labelled_comments}
        
        return render(request, 'labeler_form.html', context)
    
    if request.method == 'POST':
        print(request.POST.keys())
        tagged_labels = [l for l in labels.values_list('label_text', flat=True) if l in request.POST.keys()]
        print('tagged_labels')
        print(tagged_labels)
        comment = Comment.objects.filter(comment_id = request.POST.get('comment_id')).first()
        for label_text in tagged_labels:
            label = Labels.objects.filter(label_text=label_text).first()
            if not comment.labels.filter(id=label.id):
                comment.labels.add(label)
            LabellerMap.objects.create(user=request.user, comment=comment, label=label)
        if request.POST['new_label']:
            text, name = format_label_name(request.POST['new_label'])
            label = Labels.objects.create(label_text=text, display_text=name)
            comment.labels.add(label)
            LabellerMap.objects.create(user=request.user, comment=comment, label=label)
        
        return redirect('/labeler')











# @login_required(login_url='/login')
# def labeler_method(request):
#     if request.method == 'GET':
#         print(request.path)
#         comments = Comment.objects.filter(tags__isnull=True)
#         available_comments = len(comments)
#         comment = comments.first()
#         labelled_comments = Comment.objects.filter(tags__isnull=False).count()
#         return render(request, 'labeler_firm.html', {'comment_text': comment.comment_text, 'comment_id': comment.comment_id,
#             'video_title': comment.video_title, 'available_comments': available_comments, 'labelled_comments': labelled_comments})
#     if request.method == 'POST':
#         tags = []
#         for f in ["timestamp", "thanks", "greetings", "question", "doubt", "suggestion", "future-question", "disagree", "other", "non-english"]:
#             if f in request.POST.keys():
#                 tags.append(f)
#         if not tags:
#             return redirect('/labeler')
        
#         comment_id = request.POST.get('comment_id')
#         tags = '+'.join(tags)
#         comment = Comment.objects.filter(comment_id=comment_id).first()
#         comment.tags = tags
#         comment.save()
#         return redirect('/labeler')

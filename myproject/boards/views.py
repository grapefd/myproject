from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Board,Topic, Post
from django.contrib.auth.models import User
#w为啥加点？
# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def board_topics(request, pk):
    # board = Board.objects.get(pk=pk)
    board = get_object_or_404(Board,pk = pk)
 # 404 写成了 400
 #    try:
 #    	board = Board.objects.get(pk=pk)
	# except Board.DoesNotExist:
	# 	raise Http404
    return render(request, 'topics.html', {'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: 临时使用一个账号作为登录用户

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})
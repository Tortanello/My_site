from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from datetime import datetime
from .models import Comment_db

from .models import Article_db
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from django.urls import reverse_lazy

from django.shortcuts import redirect

# Create your views here.


class PatientDetailView(FormMixin,DetailView):
    model = Article_db
    form_class = CommentForm
    def index(request):
        return render (request, 'article/article_db_detail.html')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.user.is_authenticated: 
            if form.is_valid():
                now = datetime.now()
                now_DMYHM = (now.strftime("%Y-%m-%d %H:%M:%S"))
                comment_user = request.POST.get('comment')
                username = request.user.username 

                comments = Comment_db(date = now_DMYHM, comment = comment_user, username = username, idPost = self.get_object().id).save()
        else:
            return redirect ('http://127.0.0.1:8000/registration/')
        return HttpResponseRedirect (reverse_lazy ('article/post.html',kwargs = {'pk':self.get_object().id}))

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        context['Comment_db'] = Comment_db.objects.all().order_by('-date')
        return context


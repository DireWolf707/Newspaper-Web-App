from django.views.generic import View,CreateView,UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Article,Comment
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CommentForm

class HomeView(TemplateView):
    template_name ='home.html'
    
class ArticleListView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        articles = Article.objects.all().order_by('-created')
        return render(request,'article_list.html', {'articles': articles})

class ArticalDetailView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        article = get_object_or_404(Article,pk=self.kwargs['pk'])
        comments = article.comments.all()
        comment_form = CommentForm()
        return render(request,'article_detail.html', {'article': article,'comments':comments,'form':comment_form})
    
    def post(self,request, *args, **kwargs):
        pk=self.kwargs['pk']
        article=get_object_or_404(Article,pk=pk)
        comment = Comment(article=article,
                          comment=self.request.POST['comment'],
                          user=self.request.user)
        comment.save()
        return redirect('article_detail',pk)
    
class ArticalUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'article_update.html'
    fields = ('title','body',)
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title','body',)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,View):
    def get(self,request, *args, **kwargs):
        title = self.obj.title
        return render(request,'article_delete.html',{'title':title})
    
    def post(self,request, *args, **kwargs):
        self.obj.delete()
        return redirect('article_list',permanent=True)
    
    def test_func(self):
        self.obj = get_object_or_404(Article,pk=self.kwargs['pk'])
        return self.obj.author == self.request.user
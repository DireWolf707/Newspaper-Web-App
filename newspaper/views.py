from django.views.generic import View,CreateView,UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Article
from django.shortcuts import render,redirect,get_object_or_404

class HomeView(TemplateView):
    template_name ='home.html'
    
class ArticleListView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request,'article_list.html', {'articles': articles})

class ArticalDetailView(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        article = get_object_or_404(Article,pk=self.kwargs['pk'])
        comments = article.comments.all()
        return render(request,'article_detail.html', {'article': article,'comments':comments})
    
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
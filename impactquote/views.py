from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Quote
from .forms import PostQuote
from django.db.models import Q


def home(request):
    list=Quote.objects.all()
    form = PostQuote(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    query=request.GET.get("q")
    if query:
        list=list.filter(Q(movie__icontains=query)|Q(quote__icontains=query))
    context = {
        "form": form,
        "list": list,
    }
    return render(request,'impactquote/home.html',context)



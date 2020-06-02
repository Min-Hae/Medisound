from django.shortcuts import render
from .forms import *
import get_text
from .models import *
from django.views import generic
import os


def main(request):
    return render(request, 'main.html')


def search_drug(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            f = './media/image/'+str(request.FILES['img'])
            if not os.path.isfile(f):
                form.save()
            img_name = get_text.get_name(f)
            search = Drug.objects.filter(name__icontains=img_name).values()
            context = {'drug_list': search, 'cnt': search.count()}
            return render(request, 'test-web/search-results.html', context=context)
    else:
        form = ImgForm()
    return render(request, 'test-web/search-drug.html', {'form': form})


def text_detect(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            f = './media/image/'+str(request.FILES['img'])
            if not os.path.isfile(f):
                form.save()
            img_text = get_text.get_text(f)
            context = {'text': img_text}
            return render(request, 'test-web/text-results.html', context=context)
    else:
        form = ImgForm()
    return render(request, 'test-web/get-text.html', {'form': form})


class DrugDetailView(generic.DetailView):
    model = Drug
    template_name = 'test-web/drug-detail.html'


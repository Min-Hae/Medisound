from django.shortcuts import render, get_object_or_404
from .forms import *
import get_text
from .models import *
import os


def main(request):
    return render(request, 'main.html')


def about_service(request):
    return render(request, 'about-service.html')


def search_drug_img(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            f = './media/image/'+str(request.FILES['img'])
            form.save()
            img_name = get_text.get_name(f)
            os.remove(f)
            search = Drug.objects.filter(name__icontains=img_name).values()
            context = {'drug_list': search, 'cnt': search.count()}
            return render(request, 'test_web/search-results.html', context=context)
    else:
        form = ImgForm()
    return render(request, 'test_web/search-img.html', {'form': form})


def search_drug_name(request):
    search_name = request.GET.get('search_box', '')
    if search_name:
        result = Drug.objects.filter(name__icontains=search_name).values()
        context = {'drug_list': result, 'cnt': result.count()}
        return render(request, 'test_web/search-results.html', context=context)
    return render(request, 'test_web/search-name.html')


def drug_detail(request, pk):
    drug = get_object_or_404(Drug, pk=pk)
    context = {'drug': drug}
    return render(request, 'test_web/drug-detail.html', context=context)




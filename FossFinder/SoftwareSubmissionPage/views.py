from django.shortcuts import render
from .models import SubmittedSoftware
from .forms import SubmitSoftwareForm

# Create your views here.
def software_submit(request):
    form = SubmitSoftwareForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = SubmitSoftwareForm()

    return render(request, 'software_submit.html', {'form':form})

def software_submit_detail(request, pk):
    software = SubmittedSoftware.objects.get(pk=pk)
    context = {
        'SubmittedSoftware': software
    }
    return render(request, 'software_submit_detail.html', context)



def software_index_All(request):
    SubmittedSoftwares = SubmittedSoftware.objects.all()
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)

def software_index_MAC(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(os_MAC=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_WIN(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(os_WIN=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_NIX(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(os_NIX=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)

def software_index_tag_WordProcesser(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_WordProcesser=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_SpreadSheet(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_SpreadSheet=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_GraphicsEditor(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_GraphicsEditor=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_AudioEditor(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_AudioEditor=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_Communication(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_Communication=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_Multimedia(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_Multimedia=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_AntiVirus(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_AntiVirus=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_CodeEditor(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_CodeEditor=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_DiskBurner(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_DiskBurner=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_FileShare(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_FileShare=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
def software_index_tag_Other(request):
    SubmittedSoftwares = SubmittedSoftware.objects.filter(tag_Other=1)
    context = {
        'SubmittedSoftwares': SubmittedSoftwares
    }
    return render(request, 'software_list.html', context)
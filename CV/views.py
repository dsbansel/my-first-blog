from django.shortcuts import render
from .models import Section
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import SectionForm
from django.shortcuts import redirect
from django.http import HttpResponse


def CV(request):
    sections = Section.objects.filter()#last_edited__lte=timezone.now()).order_by('last_edited')
    return render(request, 'CV/CV_all_sections.html', {'sections': sections})

def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    return render(request, 'CV/section_detail.html', {'section': section})

def section_edit(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            section = form.save(commit=False)
            section.author = request.user
            section.last_edited = timezone.now()
            section.save()
            return redirect('section_detail', pk=section.pk)
    else:
        form = SectionForm(instance=section)
    return render(request, 'CV/section_edit.html', {'form': form})
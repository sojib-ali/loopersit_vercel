from django.shortcuts import render, get_object_or_404,redirect
from .models import Job
from .forms import ApplicationForm


def job_list(request):
    jobs = Job.objects.filter(active=True)
    return render(request, 'career/list.html', {'active':'career', 'jobs':jobs})

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'career/detail.html', {'active': 'career', 'job':job})


def apply_for_job(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('application_success')
    else:
        form = ApplicationForm()
    return render(request, 'career/apply.html', {'active': 'career', 'form': form})


def application_success(request):
    return render(request, 'success.html',{'active': 'career'})
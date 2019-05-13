from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView

from recipcraftApi.settings import LOGIN_REDIRECT_URL
from .forms import UploadForm
from .models import File


# Create your views here.
class StorageView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        elif not request.user.is_staff:
            return HttpResponseForbidden("Permission denied!")
        file = UploadForm(request.POST, request.FILES)
        if file.is_valid():
            file.save()
            return HttpResponseRedirect(reverse('storage'))

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        elif not request.user.is_staff:
            return HttpResponseForbidden("Permission denied!")
        file = UploadForm()
        files = File.objects.all().order_by('-upload_date')
        context = {
            'form': file,
            'files': files,
            'redirect_url': LOGIN_REDIRECT_URL
        }
        return render(request, 'app_storage/storage.html', context)


class FileDelete(DeleteView):
    model = File
    success_url = reverse_lazy('storage')
    template_name = 'app_storage/delete_file.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        elif not request.user.is_staff:
            return HttpResponseForbidden("Permission denied!")
        self.object = self.get_object()
        self.success_url = self.get_success_url()
        self.object.delete()
        return redirect(reverse('storage'))

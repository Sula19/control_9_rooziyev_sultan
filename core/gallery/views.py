from django.shortcuts import render, redirect
from .models import Gallery
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from .forms import GalleryForm


class GalleryListView(ListView):
    template_name = 'index.html'
    model = Gallery
    context_object_name = 'galleries'
    paginate_by = 5
    ordering = ('-created_at',)


class GalleryCreateView(CreateView):
    template_name = 'create_gallery.html'
    model = Gallery
    form_class = GalleryForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.author = self.request.user
            form.save()
            return redirect('/')
        context = {'form': form}
        return self.render_to_response(context)


class GalleryUpdateView(UpdateView):
    template_name = 'gallery_update.html'
    model = Gallery
    form_class = GalleryForm
    success_url = '/'


class GalleryDetailView(DetailView):
    template_name = 'gallery_detail.html'
    model = Gallery
    context_object_name = 'gallery'


class GalleryDeleteView(DeleteView):
    template_name = 'gallery_delete.html'
    model = Gallery
    success_url = '/'

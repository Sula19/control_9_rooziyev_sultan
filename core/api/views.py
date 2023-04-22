from django.shortcuts import render
from gallery.models import Gallery
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def favorite_api_view(request, *args, **kwargs):
    if request.method == 'POST':
        user = request.user
        gallery = Gallery.objects.get(pk=kwargs.get('pk'))
        if user not in gallery.favorite.all():
            gallery.favorite.add(user)
        else:
            gallery.favorite.remove(user)
        return JsonResponse({'status': 'ok'})

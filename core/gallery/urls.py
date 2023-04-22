from django.urls import path
from .views import (GalleryListView,
                    GalleryCreateView,
                    GalleryUpdateView,
                    GalleryDetailView,
                    GalleryDeleteView)

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery-list'),
    path('gallery/create', GalleryCreateView.as_view(), name='gallery-create'),
    path('gallery/<int:pk>/update', GalleryUpdateView.as_view(), name='gallery-update'),
    path('gallery/<int:pk>/detail', GalleryDetailView.as_view(), name='gallery-detail'),
    path('gallery/<int:pk>/delete', GalleryDeleteView.as_view(), name='gallery-delete'),
]

from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Index,name="teacher_form"),
    path('reg/',views.teacher_registration.as_view(),name='registration'),
    path('table/',views.Table.as_view(),name='table'),
    path('delete/<int:uid>/',views.Delete.as_view(),name='delete'),
    path('update/<int:uid>/',views.update,name='update'),
    path('edit/',views.teacher_update,name='edit'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
import crudapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',crudapp.views.index, name = "index"),
    path('new',crudapp.views.new, name = 'new'),
    path('create',crudapp.views.create, name = 'create'),
    path('<int:blog_id>', crudapp.views.detail, name = "detail"),
    path('blog/edit/<int:blog_id>', crudapp.views.edit, name = 'edit'),
    path('blog/delete/<int:blog_id>', crudapp.views.delete, name = 'delete'),
    path('portfolio/', portfolio.views.portfolio, name = 'portfolio'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

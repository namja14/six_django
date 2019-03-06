from django.contrib import admin
from django.urls import path, include
import catsite.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', catsite.views.home, name = "home"),
    path('about/', catsite.views.about, name ="about"),
    path('accounts/', include('allauth.urls')),
    path('new/',catsite.views.new, name="new"),
    path('', blog.views.portfolio, name = "home"),
    path('detail/<int:portfolio_id>',blog.views.p_detail, name = "p_detail"),
    path('create/',catsite.views.create, name = "create")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
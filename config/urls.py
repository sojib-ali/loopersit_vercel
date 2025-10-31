from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('lit-admin/', admin.site.urls),
    path('', include('loopers.urls')),
    path('career/', include('career.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


admin.site.index_title = 'LoopersIT'
admin.site.site_header = 'LoopersIT Admin'
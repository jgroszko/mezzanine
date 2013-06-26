from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.utils.static import static_lazy as static

class GalleryImageInline(TabularDynamicInlineAdmin):
    model = GalleryImage

class GalleryAdmin(PageAdmin):

    exclude = ['zip_import',]

    class Media:
        css = {"all": (static("mezzanine/css/admin/gallery.css"),)}
        js = {"mezzanine/js/admin/gallery.js",}

    inlines = (GalleryImageInline,)

admin.site.register(Gallery, GalleryAdmin)

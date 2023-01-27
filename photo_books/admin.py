from django.contrib import admin
from .models import PhotoBook, PhotoBookComment, PhotoBookPortfolio


class PhotoBookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class PhotoBookPortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(PhotoBook, PhotoBookAdmin)
admin.site.register(PhotoBookComment)
admin.site.register(PhotoBookPortfolio, PhotoBookPortfolioAdmin)
from django.contrib import admin
from .models import Movie, Portfolio


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Portfolio, PortfolioAdmin)


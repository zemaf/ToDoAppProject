from django.contrib import admin

from .models import Task

# 1ere méthode : utiliser admin.site.register(Task)

# 2eme méthode plus pratique : on indique au décorateur quel modèle on veut administrer
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass  # on pourra ajouter beaucoup plus d'options par la suite

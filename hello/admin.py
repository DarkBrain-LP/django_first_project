from django.contrib import admin
from hello.models import Etudiant

# Register your models here.

# We use the auto generation to generate a view basing on our model
admin.site.register(Etudiant)
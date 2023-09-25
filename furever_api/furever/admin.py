from django.contrib import admin
from .models import (Animal,
                    AnimalVenta,
                    AnimalAdopcion,
                    UserApp,
                    Interesado,
                    Oferente,
                    Foto,
                    Documentacion,
                    Conexion,
                    )
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class UserAppInLine(admin.StackedInline):
    model = UserApp
    can_delete = False
    verbose_name_plural = "userapp"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserAppInLine]

admin.site.register(Animal)
admin.site.register(AnimalVenta)
admin.site.register(AnimalAdopcion)
admin.site.register(UserApp)
admin.site.register(Interesado)
admin.site.register(Oferente)
admin.site.register(Foto)
admin.site.register(Documentacion)
admin.site.register(Conexion)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

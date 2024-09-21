"""Configuração do meu admin.

"""

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from authentication.models import User
from jogos.models import Equipes,Jogador,Jogadores_em_equipes, Modalidade

@admin.register(Equipes)
class Equipes(admin.ModelAdmin):
   

   list_display = ["nome","modalidade",]



@admin.register(Modalidade)
class Modalidade(admin.ModelAdmin):
   

   list_display = ["nome","tipo","categoria","min_jogadores",]

@admin.register(Jogador)
class Jogador(admin.ModelAdmin):

   list_display = ["nome"]


@admin.register(Jogadores_em_equipes)
class Jogadores_equipes(admin.ModelAdmin):
   

   list_display = ["jogador","equipe"]




class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "is_active",
            "is_superuser",
            "is_staff",
        ]


class MyUserAdmin(BaseUserAdmin):
    form = UserChangeForm

    list_display = ["email", "first_name", "last_name", "is_superuser", "is_staff"]
    list_filter = ["is_superuser", "is_staff"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, MyUserAdmin)

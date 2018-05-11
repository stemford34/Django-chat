from django.contrib import admin

from registration.models import UserInfo
from .models import DialogInfo, DialogMassage, DialogUsers

admin.site.register(UserInfo)
admin.site.register(DialogInfo)
admin.site.register(DialogMassage)
admin.site.register(DialogUsers)
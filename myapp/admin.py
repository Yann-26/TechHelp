from django.contrib import admin
from .models import Contact, Banner,\
    Navbar, Topbar, contactUs, Comment#, TeamMembers

# Register your models here.
admin.site.register(Contact)
admin.site.register(Topbar)
admin.site.register(Navbar)
admin.site.register(Banner)
admin.site.register(contactUs)
admin.site.register(Comment)
# admin.site.register(TeamMembers)

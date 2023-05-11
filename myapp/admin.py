from django.contrib import admin
from .models import Contact, Banner,\
    Navbar, Topbar, contactUs, Comment, TeamMembers, Reponse_Commentaire,  Subscriber, Newsletter, Policy


def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)

# Register your models here.
admin.site.register(Contact)
admin.site.register(Topbar)
admin.site.register(Policy)
admin.site.register(Navbar)
admin.site.register(Banner)
admin.site.register(contactUs)
admin.site.register(Comment)
admin.site.register(TeamMembers)
admin.site.register(Reponse_Commentaire)

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from .models import Subscriber
# from newsletter.forms import SubscriberForm
# import random
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# from django.core.mail import send_mail

# # Helper Functions
# def random_digits():
#     return "%0.12d" % random.randint(0, 999999999999)


# #request.build_absolute_uri() garantit que l'URL absolue est correcte à la fois dans l'environnement local et dans un environnement déployé
# @csrf_exempt
# def new(request):
#     if request.method == 'POST':
#         sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
#         sub.save()
#         email_subject = 'Newsletter Confirmation'
#         email_body = 'Thank you for signing up for my email newsletter! \
#                 Please complete the process by \
#                 <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
#                 confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
#                                                     sub.email,
#                                                     sub.conf_num)
#         send_mail(email_subject, email_body, settings.FROM_EMAIL, [sub.email], html_message=email_body)
#         return render(request, 'base.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
#     else:
#         return render(request, 'base.html', {'form': SubscriberForm()})


# ####VUE DE CONFIRMATION A LA SOUSCRIPTION PAR EMAIL
# def confirm(request):
#     sub = Subscriber.objects.get(email=request.GET('email'))
#     if sub.conf_num == request.GET['conf_num']:
#         sub.confirmed = True
#         sub.save()
#         return render(request, 'principal/index.html', {'email': sub.email, 'action': 'confirmed'})
#     else:
#         return render(request, 'principal/index.html', {'email': sub.email, 'action': 'denied'})


# ### DESOUSCRIPTION 
# def delete(request):
#     sub = Subscriber.objects.get(email=request.GET('email'))
#     if sub.conf_num == request.GET['conf_num']:
#         sub.delete()
#         return render(request, 'principal/index.html', {'email': sub.email, 'action': 'unsubscribed'})
#     else:
#         return render(request, 'principal/index.html', {'email': sub.email, 'action': 'denied'})


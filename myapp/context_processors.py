from .forms import SubscriberForm

def newsletter_form(request):
    form = SubscriberForm()
    return {'newsletter_form': form}

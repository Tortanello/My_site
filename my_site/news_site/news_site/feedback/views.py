from django.shortcuts import render
from .forms import Feedback_form
from .models import Feedback
from datetime import datetime
# Create your views here.
def feedback(request):
    form_feedback = Feedback_form
    if request.method == "POST":
        username = request.user.username
        proposal = request.POST.get("proposal")
        now = datetime.now()
        now_DMYHM = (now.strftime("%Y-%m-%d %H:%M:%S"))

        proposal_post = Feedback(date = now_DMYHM, proposal = proposal, username = username).save()
        return render(request, 'form_send_feedback.html', {'username':username})
    else:
        return render(request, 'form_feedback.html', {'form_feedback':form_feedback})
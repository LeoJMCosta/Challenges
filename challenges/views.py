from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for a whole month!",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Learn Python for at least 20 minutes every day.",
    "april": "Meditate for at least 10 minutes daily.",
    "may": "Read at least 10 pages of a book every day.",
    "june": "Drink at least 8 glasses of water each day.",
    "july": "Wake up early and watch the sunrise at least once a week.",
    "august": "Write in a journal every day.",
    "september": "Try a new recipe each week.",
    "october": "Do a random act of kindness every day.",
    "november": "Practice gratitude by writing down three things you are grateful for each day.",
    "december": None
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1 or month > len(months):
        return HttpResponseNotFound('Invalid Month')
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)

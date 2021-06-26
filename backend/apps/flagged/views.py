from django.shortcuts import render
from .models import FlaggedSite


def flagged_sites(request):
    sites = FlaggedSite.objects.all()
    unverified = sites.filter(count__lte=2)
    unrelaible = sites.filter(count__lte=5).filter(count__gt=2)
    fakenews = sites.filter(count__gt=5)

    data = {
        'unverified': unverified,
        'unreliable': unrelaible,
        'fakenews': fakenews
    }

    return render(request, 'flagged/index.html', data)

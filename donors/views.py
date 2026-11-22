from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .constants import BLOOD_GROUPS, DISTRICTS
from .forms import BecomeDonorForm, BloodRequestForm, ProfileForm, SignupForm
from .models import BloodRequest, Donor
from .utils import distance_km


def home(request):
    today = timezone.localdate()
    requests_qs = BloodRequest.objects.filter(status="open", needed_date__gte=today)[:6]
    donors = list(Donor.objects.order_by("-created_at"))
    available = [d for d in donors if d.is_available]
    return render(request, "donors/home.html", {
        "blood_requests": requests_qs,
        "total_donors": len(donors),
        "available_donors": len(available),
        "featured_donors": available[:6],  
    })
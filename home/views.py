from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import action
from django.db.models import Q
from config.models import user_types, GmailUser

"""api view"""


@login_required
@action(detail=False, methods=['get', 'post'])
def home(request):
    context = {'popup': False}

    if request.method == 'POST':
        """save the user data"""
        user = request.user
        user.type = request.POST.get('type')
        user.phone = request.POST.get('phone')
        user.institution = request.POST.get('institution')
        user.saved = True
        user.save()
        context["popup"] = True

    if request.user.is_staff:
        return redirect('admin:index')

    context = {
        **context,
        "name": request.user.get_full_name(),
        "email": request.user.email,
        "phone": request.user.phone or "",
        "type": request.user.type,
        "institution": request.user.institution or "",
        "user_types": user_types,
        "saved": request.user.saved,
    }

    return render(request, "home/home.html", context=context)


@login_required
def institutions(request):
    """json response of all institutions"""
    return JsonResponse({
        "institutions": list(GmailUser.objects.filter(institution__icontains=request.GET.get('q'))
                             .distinct()[:20]
                             .values_list("institution", flat=True))
    })

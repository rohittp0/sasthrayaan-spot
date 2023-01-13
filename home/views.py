from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework.decorators import action


@login_required
@action(detail=False, methods=['get'])
def home(request):
    if request.user.is_staff:
        return redirect('admin:index')

    context = {
        "name": request.user.get_full_name(),
        "email": request.user.email,
        "phone": request.user.phone,
        "type": request.user.type,
        "institution": request.user.department,
    }

    return render(request, "home/home.html", context=context)

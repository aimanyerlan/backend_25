from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Table
from .forms import TableForm
from reservations.models import Reservation

def tables_list(request):
    tables = Table.objects.all()
    return render(request, "tables/tables_list.html", {"tables": tables})

@login_required
def create_table(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tables_list")
    else:
        form = TableForm()
    return render(request, "tables/tables_list.html", {"form": form})


def available_tables(request):
    date = request.GET.get("date")
    time = request.GET.get("time")
    if not date or not time:
        return JsonResponse({"error": "Date and time are required"}, status=400)

    reserved_tables = Reservation.objects.filter(date=date).values_list("table_id", flat=True)

    available_tables = Table.objects.exclude(id__in=reserved_tables)
    
    return render(request, "tables/tables_available.html", {"tables": available_tables, "date": date, "time": time})

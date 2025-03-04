from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Reservation
from .forms import ReservationForm

@login_required
def reservation_list_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            table = form.cleaned_data["table"]
            date = form.cleaned_data["date"]

            # Проверка на существующие бронирования
            if Reservation.objects.filter(user=user, date=date).exists():
                return JsonResponse({"error": "This user already has a reservation on this date"}, status=400)
            
            if Reservation.objects.filter(table=table, date=date).exists():
                return JsonResponse({"error": "This table is already reserved on this date"}, status=400)
            
            form.save()
            return redirect('user_reservations', user_id=user.id)
    else:
        form = ReservationForm()

    reservations = Reservation.objects.all()
    return render(request, 'reservations_list.html', {'reservations': reservations, 'form': form})
def create_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations_list')  # После создания брони перенаправляем на список бронирований
    else:
        form = ReservationForm()
    return render(request, 'reservations/create_reservation.html', {'form': form})


def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(user_id=user_id)
    return render(request, 'user_reservations.html', {'reservations': reservations})

@login_required
def update_reservation_status(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        status = request.POST.get("status")
        if status not in dict(Reservation.STATUS_CHOICES):
            return JsonResponse({"error": "Invalid status"}, status=400)
        reservation.status = status
        reservation.save()
        return redirect('reservation_detail', id=reservation.id)
    return render(request, 'update_reservation.html', {'reservation': reservation})

@login_required
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return redirect('user_reservations', user_id=reservation.user.id)

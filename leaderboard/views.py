from django.shortcuts import render, redirect, get_object_or_404
from .forms import GameForm, PlayerForm
from .models import TotalLeaderboard, DailyLeaderboard
from django.contrib.auth.decorators import login_required


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


@login_required
def create_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leaderboard:daily_leaderboard")
    else:
        form = GameForm()
    return render(request, "create_game.html", {"form": form})


@login_required
def create_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leaderboard:create_game")
    else:
        form = PlayerForm()
    return render(request, "create_player.html", {"form": form})


def total_leaderboard(request):
    TotalLeaderboard.update_total_leaderboard()
    total_leaderboard = TotalLeaderboard.objects.order_by("-total_score")
    return render(
        request,
        "total_leaderboard.html",
        {"total_leaderboard": total_leaderboard},
    )


def daily_leaderboard(request, date=None):
    if date:
        daily_leaderboard = DailyLeaderboard.objects.filter(
            date=date).order_by(
            "-score", "player__name"
        )
        return render(
            request,
            "daily_leaderboard_detail.html",
            {"date": date, "daily_leaderboard": daily_leaderboard},
        )
    else:
        dates_with_games = (
            DailyLeaderboard.objects.order_by("date")
            .values_list("date", flat=True)
            .distinct()
        )
        return render(
            request,
            "daily_leaderboard.html",
            {"dates_with_games": dates_with_games},
        )


@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(DailyLeaderboard, id=entry_id)
    if request.method == "POST":
        form = GameForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect(
                "leaderboard:daily_leaderboard_detail",
                date=entry.date
                )
    else:
        form = GameForm(instance=entry)
    return render(request, "edit_entry.html", {"form": form})


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(DailyLeaderboard, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect(
            'leaderboard:daily_leaderboard_detail',
            date=entry.date
            )
    return render(request, 'delete_entry.html', {'entry': entry})

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Member
from .models import Member, Workout
from .forms import MemberForm


def index(request):

    members = Member.objects.all()

    total_members = members.count()

    if total_members > 0:

        avg_weight = round(

            sum([m.weight for m in members])
            / total_members,

            2

        )

    else:

        avg_weight = 0

    context = {

        'members': members,

        'total_members': total_members,

        'avg_weight': avg_weight,

    }

    return render(
        request,
        'index.html',
        context
    )


def add_member(request):

    if request.method == 'POST':

        form = MemberForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = MemberForm()

    return render(
        request,
        'add_member.html',
        {'form': form}
    )


def edit_member(request, id):

    member = get_object_or_404(
        Member,
        id=id
    )

    if request.method == 'POST':

        form = MemberForm(
            request.POST,
            instance=member
        )

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = MemberForm(
            instance=member
        )

    return render(
        request,
        'edit_member.html',
        {'form': form}
    )


def delete_member(request, id):

    member = get_object_or_404(
        Member,
        id=id
    )

    member.delete()

    return redirect('home')
from .forms import WorkoutForm


def add_workout(request):

    if request.method == 'POST':

        form = WorkoutForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = WorkoutForm()

    return render(
        request,
        'add_workout.html',
        {'form': form}
    )
from .forms import WorkoutForm


def add_workout(request, member_id):

    member = get_object_or_404(
        Member,
        id=member_id
    )

    if request.method == 'POST':

        form = WorkoutForm(request.POST)

        if form.is_valid():

            workout = form.save(commit=False)

            workout.member = member

            workout.save()

            return redirect('home')

    else:

        form = WorkoutForm()

    return render(

        request,

        'add_workout.html',

        {
            'form': form,
            'member': member
        }
    )
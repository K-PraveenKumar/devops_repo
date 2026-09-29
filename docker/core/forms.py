from django import forms

from .models import (
    Member,
    Workout
)


class MemberForm(forms.ModelForm):

    class Meta:

        model = Member

        fields = '__all__'


class WorkoutForm(forms.ModelForm):

    class Meta:

        model = Workout

        exclude = ['member']
from django.db import models


class Member(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    height = models.FloatField(
        help_text='Height in cm'
    )

    weight = models.FloatField(
        help_text='Weight in kg'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def bmi(self):

        height_m = self.height / 100

        bmi_value = self.weight / (height_m ** 2)

        return round(bmi_value, 2)

    def __str__(self):
        return self.name


class Workout(models.Model):

    EXERCISE_CHOICES = [

        ('Push Ups', 'Push Ups'),
        ('Pull Ups', 'Pull Ups'),
        ('Squats', 'Squats'),
        ('Bench Press', 'Bench Press'),
        ('Deadlift', 'Deadlift'),
        ('Bicep Curls', 'Bicep Curls'),
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),

    ]

    CALORIE_MAP = {

        'Push Ups': 40,
        'Pull Ups': 50,
        'Squats': 45,
        'Bench Press': 70,
        'Deadlift': 90,
        'Bicep Curls': 35,
        'Running': 100,
        'Cycling': 80,
    }

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    exercise = models.CharField(
        max_length=100,
        choices=EXERCISE_CHOICES
    )

    sets = models.IntegerField()

    reps = models.IntegerField()

    calories_burned = models.IntegerField(
        editable=False,
        default=0
    )

    workout_date = models.DateField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        base_calories = self.CALORIE_MAP.get(
            self.exercise,
            30
        )

        self.calories_burned = (
            base_calories *
            self.sets *
            self.reps
        ) // 10

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.member.name} - {self.exercise}"


class Diet(models.Model):

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    meal_name = models.CharField(
        max_length=100
    )

    calories = models.IntegerField()

    protein = models.FloatField()

    carbs = models.FloatField()

    fats = models.FloatField()

    def __str__(self):

        return self.meal_name
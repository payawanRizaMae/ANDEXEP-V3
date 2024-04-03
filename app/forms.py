from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import AppUser


class StressLevelForm(forms.Form):
    GENDER_CHOICES = [(1, 'Male'), (0, 'Female')]
    BMI_CATEGORY_CHOICES = [
        (0, 'Normal'), (3, 'Underweight'), (2, 'Overweight'), (1, 'Obese')
    ]

    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    bmi_category = forms.ChoiceField(
        choices=BMI_CATEGORY_CHOICES, label='BMI Category')
    phq1 = forms.ChoiceField(
        label='PHQ-1. Little interest or pleasure in doing things?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq2 = forms.ChoiceField(
        label='PHQ-2. Feeling down, depressed, or hopeless?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq3 = forms.ChoiceField(
        label='PHQ-3.  Trouble falling or staying asleep, or sleeping too much?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq4 = forms.ChoiceField(
        label='PHQ-4. Feeling tired or having little energy?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq5 = forms.ChoiceField(
        label='PHQ-5. Poor appetite or overeating?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq6 = forms.ChoiceField(
        label='PHQ-6.  Feeling bad about yourself or that you are a failure or have let yourself or your family down?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq7 = forms.ChoiceField(
        label='PHQ-7.  Trouble concentrating on things, such as reading the books or watching television?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq8 = forms.ChoiceField(
        label='PHQ-8.  Moving or speaking so slowly that other people could have noticed. Or the opposite being so fidgety or restless that you have been moving around a lot more than usual?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )
    phq9 = forms.ChoiceField(
        label='PHQ-9.  Thoughts that you would be better off dead, or of hurting yourself?',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')],
        widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        super(StressLevelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = ''


class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('name',) + UserCreationForm.Meta.fields

from django import forms
from material import *
import datetime


class PredictionForm(forms.Form):
    project_title = forms.CharField(label="Project Title")
    lead = forms.CharField()
    service_line = forms.CharField(label="Service Line")
    difficulty_choices = (
        ('?     Easy', '?     Easy'),
        ('?     Medium','?     Medium'),
        ('?     Hard', '?     Hard'),
    )
    type_choices = (
        ('CI Project', 'CI Project'),
        ('O', 'O'),
        ('Ops Action', 'Ops Action'),
        ('SLI', 'SLI'),
        ('CSWP', 'CSWP'),
        ('SW', 'SW'),
        ('Bus Devel', 'Bus Devel'),
        ('Lateral Deployment', 'Lateral Deployment'),
        ('VSM', 'VSM'),
    )
    difficulty = forms.ChoiceField(label="Difficulty", choices=difficulty_choices)
    project_type = forms.ChoiceField(label="Type", choices=type_choices)
    priority_choices = (
        ('!', '!'),
        ('!!', '!!'),
        ('!!!','!!!'),
    )
    priority = forms.ChoiceField(label="Priority", choices=priority_choices)
    priority_num = forms.IntegerField(label="Priority Number")
    status = forms.CharField()
    status_num = forms.IntegerField(label="Status Number")
    identifier = forms.CharField()
    date_entered = forms.DateField(initial=datetime.date.today)
    actual_start = forms.DateField(initial=datetime.date.today)
    target_finish = forms.DateField(initial=datetime.date.today)
    actual_finish = forms.DateField(initial=datetime.date.today)
    late_finsih = forms.IntegerField(label="Late Finish")
    # projected_savings_choices = (
    #     ('0', 'No'),
    #     ('1', 'Yes'),
    # )
    projected_annual_savings = forms.IntegerField(label="Projected Annual Savings")
    savings_year = forms.IntegerField(label="Savings Year")
    year = forms.IntegerField()
    region_choices = (
        ('North Region', 'North Region'),
        ('Central Entities', 'Central Entities'),
    )
    region = forms.ChoiceField(choices=region_choices)
    facility_choices = (
        ('Bear River', 'Bear River'),
        ('Cassia', 'Cassia'),
        ('Logan', 'Logan'),
        ('McKay-Dee', 'McKay-Dee'),
        ('RCO', 'RCO'),
        ('Risk Mgmt', 'Risk Mgmt'),
    )
    facility = forms.ChoiceField(choices=facility_choices)
    ops_officer = forms.CharField(label="Ops Officer")
    director = forms.CharField()
    system_choices = (
        ('Intermountain Healthcare', 'Intermountain Healthcare'),
    )
    system = forms.ChoiceField(choices=system_choices)
    yesno = (('0', 'No'), ('1', 'Yes'),)
    month = forms.ChoiceField(choices=yesno)
    week = forms.ChoiceField(choices=yesno)
    active_queue_flag = forms.ChoiceField(choices=yesno)
    active_flag = forms.ChoiceField(choices=yesno)
    active_complete_flag = forms.ChoiceField(choices=yesno)
    queue_time = forms.CharField(label="Queue Time (weeks)")
    duration = forms.CharField(label="Duration (weeks)")
    # 'YEAR_END': "1",
    # 'YEAR_TODAY': "1",
    # 'TALLY': "1",
    tally_c = forms.ChoiceField(choices=yesno)
    physician_involvement = forms.ChoiceField(choices=yesno)
    physician_led = forms.ChoiceField(choices=yesno)
    safety_flag = forms.ChoiceField(choices=yesno)
    cost_savings = forms.ChoiceField(choices=yesno)
    status_choices = (
        ('Behind', 'Behind'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
        ('On-Track', 'On-Track'),
        ('Queue', 'Queue'),
    )
    validated_flag = forms.ChoiceField(choices=yesno)
    status_flag = forms.ChoiceField(choices=status_choices)
    cancel_flag = forms.ChoiceField(choices=yesno)

    layout = Layout(Row('project_title','lead', 'service_line'),
                    Row('difficulty','project_type', 'priority', 'priority_num'),
                    Row('status', 'status_num', 'identifier'),
                    Row('date_entered', 'actual_start', 'target_finish', 'actual_finish'),
                    Row('late_finsih', 'projected_annual_savings', 'savings_year', 'year'),
                    Row('region', 'facility', 'ops_officer', 'director', 'system'),
                    Row('month', 'week', 'active_queue_flag', 'active_complete_flag', 'active_flag', 'queue_time', 'duration'),
                    Row('tally_c', 'physician_involvement', 'physician_led', 'safety_flag'),
                    Row('cost_savings', 'validated_flag', 'status_flag', 'cancel_flag'),
                    )

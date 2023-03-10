from django import forms
from webapp.models import Task, Type, Status, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.SelectMultiple)
        status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), widget=forms.RadioSelect)
        fields = {'description', 'detailed_description', 'status', 'type', 'project'}
        labels = {
            'description': 'Описание',
            'detailed_description': 'Подробно',
            'status': 'Статус',
            'type': 'Тип',
            'project': 'Проект'
        }
        widgets = {
            'status': forms.RadioSelect,
            'type': forms.SelectMultiple
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = {'title', 'description', 'start_date', 'end_date'}
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'start_date': 'Начало',
            'end_date': 'Конец',
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


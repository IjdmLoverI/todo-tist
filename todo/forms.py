from django import forms

from todo.models import Tag, Task


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


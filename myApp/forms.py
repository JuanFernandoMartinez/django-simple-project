from django import forms


class createNewTaskForm(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200, required=True )
    description = forms.CharField(widget=forms.Textarea, label="descripción de la tarea",  max_length=900, required=True )
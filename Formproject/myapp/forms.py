from django import forms

class StudnetForm(forms.Form):
    name=forms.CharField()
    usn=forms.CharField()
    mob=forms.IntegerField()
    branch=forms.CharField()
    gmail=forms.CharField()
    
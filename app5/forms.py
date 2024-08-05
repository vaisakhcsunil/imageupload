from django import forms
from .models import imageuplaoad
# class createforms(forms.Modelform):
#     class meta:
#         model=student
#         fields=[
#             "name",
#             "phonenumber",
#         ]
class imageform(forms.ModelForm):
    class Meta:
        model=imageuplaoad
        fields=['image']

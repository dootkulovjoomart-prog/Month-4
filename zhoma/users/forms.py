from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        data = self.cleaned_data
        if data.get("password") != data.get("password2"):
            raise forms.ValidationError("password must be same ")

        return data


class SignInForm(forms.Form):
     username = forms.CharField()
     password = forms.CharField()
    
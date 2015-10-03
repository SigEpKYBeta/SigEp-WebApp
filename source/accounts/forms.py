from django import forms

class RegistrationForm(forms.Form):
	first_name = forms.CharField(error_messages={'required': 'Please enter your first name.'})
	last_name = forms.CharField(error_messages={'required': 'Please enter your last name.'})
	email = forms.EmailField(error_messages={'required': 'Please enter your email.',
											 'invalid': 'Please enter a valid email.'}) 
	password = forms.CharField(widget=forms.PasswordInput,
								error_messages={'required': 'Please enter your password.'})
	reenter_password = forms.CharField(widget=forms.PasswordInput, 
										error_messages={'required': 'Please reenter your password.'})

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get('password')
		rennter_password = cleaned_data.get('reenter_password')

		if password and rennter_password:
			if password != rennter_password:
				self.add_error('password', "Your passwords did not match. Try again.")

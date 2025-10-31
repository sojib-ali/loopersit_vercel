from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class':'contact-name'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'placeholder':'Your Email', 'class':'contact-email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Subject', 'class':'contact-subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your message', 'class':'contact-message'}))
    
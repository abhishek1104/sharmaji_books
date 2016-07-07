from django import forms


class ContactForm(forms.Form):
    subject=forms.CharField(max_length=100)
    email=forms.EmailField(required=False,label="Your email address")
    message=forms.CharField(widget=forms.Textarea)

    def clean_message(self): #system auto looks for method starting with clean_ !
        message=self.cleaned_data['message']
        num_words=len(message.split())
        if num_words<10:
            raise forms.ValidationError('''Not enough words.
                Enter atleast 10 words''')

        return message #Returns the same message so that we could modify it.
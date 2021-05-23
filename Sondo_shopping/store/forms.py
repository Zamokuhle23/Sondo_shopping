from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse

from store.models import Comment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CartForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Street,City,Country'})
    )

    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-cart-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('submit_form')
        self.helper.add_input(Submit('submit', 'Submit'))

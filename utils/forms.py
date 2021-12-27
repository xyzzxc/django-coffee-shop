from django import forms


class DeleteConfirmFrom(forms.Form):
    check = forms.BooleanField(label='確定要刪除嗎？')

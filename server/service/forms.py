from core.mixins import AddClassNameMixin

from django.forms import ModelForm
from .models import FeedbackRequest

class FeedbackRequestForm(AddClassNameMixin, ModelForm):
    class Meta:
        model = FeedbackRequest
        fields = [
            'name',
            'email',
            'website',
            'content',
        ]
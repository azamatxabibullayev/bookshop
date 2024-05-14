from django.forms import ModelForm

from products.models import Review


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']
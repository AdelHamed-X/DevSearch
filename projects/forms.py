""" All forms related to projects app """
from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    """ Custom project creation form """
    class Meta:
        """ Metadata for project creation form """
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

    def __init__(self, *args, **kwargs):
        """ Custom inistantiation for form object """
        super(ProjectForm, self).__init__(*args, **kwargs)

        for k, v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})

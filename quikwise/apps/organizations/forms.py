from apps.organizations.models import Organization
from apps.organizations.services import is_name_available
from django import forms


class OrganizationAdminForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name is not None and not is_name_available(name, self.instance):
            raise forms.ValidationError("The name already exists.")

        return name


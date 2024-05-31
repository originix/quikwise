from apps.organizations.models import Organization
from django import forms


class OrganizationAdminForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name is not None and Organization.all_objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("The name already exists.")

        return name


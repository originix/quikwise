from apps.organizations.models import Organization


def is_name_available(name: str, organization: Organization = None) -> bool:
     qs = Organization.all_objects.filter(name=name)

     if organization:
          qs = qs.exclude(pk=organization.pk)

     return not qs.exists()

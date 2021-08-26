from graphene_django import DjangoObjectType
import graphene
from .models import Organization


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization


class Query(graphene.ObjectType):
    organization = graphene.Field(OrganizationType,
                                  id=graphene.ID(required=True))
    organizations = graphene.List(OrganizationType)

    def resolve_organization(root, info, id):
        try:
            return Organization.objects.get(id=id)
        except Organization.DoesNotExist:
            return None

    def resolve_organizations(root, info):
        return Organization.objects.filter(name__startswith="Ce")
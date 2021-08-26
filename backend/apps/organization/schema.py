from graphene.types import interface
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
        return Organization.objects.all()


class CreateOrganizationMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    organization = graphene.Field(OrganizationType)

    @classmethod
    def mutate(cls, root, info, name):
        organization = Organization.objects.create(name=name)
        # Notice we return an instance of this mutation
        return CreateOrganizationMutation(organization=organization)


class DeleteOrganizationMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            organization = Organization.objects.get(pk=id)
            organization.delete()
        except Organization.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteOrganizationMutation(deleted=deleted)


class Mutation(graphene.ObjectType):
    create_organization = CreateOrganizationMutation.Field()
    delete_organization = DeleteOrganizationMutation.Field()
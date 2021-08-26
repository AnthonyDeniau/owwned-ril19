from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Documentation


class DocumentationType(DjangoObjectType):
    class Meta:
        model = Documentation


class Query(graphene.ObjectType):
    documentation = graphene.Field(DocumentationType,
                                  id=graphene.ID(required=True))
    documentations = graphene.List(DocumentationType)

    def resolve_documentation(root, info, id):
        try:
            return Documentation.objects.get(id=id)
        except Documentation.DoesNotExist:
            return None

    def resolve_documentations(root, info):
        return Documentation.objects.all()


class CreateDocumentationMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    documentation = graphene.Field(DocumentationType)

    @classmethod
    def mutate(cls, root, info, name, asset, description, URL, file):
        documentation = Documentation.objects.create(name=name, asset=asset, description=description, URL=URL, file=file)

        # Notice we return an instance of this mutation
        return CreateDocumentationMutation(documentation=documentation)


class DeleteDocumentationMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            documentation = Documentation.objects.get(id=id)
            documentation.delete()
        except Documentation.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteDocumentationMutation(deleted=deleted)


class Mutation(graphene.ObjectType):
    create_documentation = CreateDocumentationMutation.Field()
    delete_documentation = DeleteDocumentationMutation.Field()

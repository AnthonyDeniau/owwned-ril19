import graphene
from apps.organization import schema as organization_schema
from apps.documentation import schema as documentation_schema

class Query(organization_schema.Query, documentation_schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(organization_schema.Mutation, documentation_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

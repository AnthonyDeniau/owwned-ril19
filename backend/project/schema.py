import graphene
from apps.organization import schema as organization_schema


class Query(organization_schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
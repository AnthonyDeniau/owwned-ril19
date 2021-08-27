import graphene
from apps.organization import schema as organization_schema
from apps.supplier import schema as supplier_schema
from apps.asset import schema as asset_schema


class Query(organization_schema.Query, asset_schema.Query,  supplier_schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Mutation(organization_schema.Mutation, supplier_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
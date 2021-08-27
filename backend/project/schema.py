import graphene
from apps.organization import schema as organization_schema
from apps.team import schema as team_schema
from apps.userprofile import schema as user_profile_schema


class Query(organization_schema.Query,team_schema.Query,user_profile_schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(organization_schema.Mutation,team_schema.Mutation,user_profile_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
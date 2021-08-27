
from django.contrib.auth.models import User
from django.db.models import fields, manager
from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Team

class UserType(DjangoObjectType):
    class Meta:
        model = User


class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class Query(graphene.ObjectType):
    team = graphene.Field(TeamType,
                                  id=graphene.ID(required=True))
    teams = graphene.List(TeamType)

    def resolve_team(root, info, id):
        try:
            return Team.objects.get(id=id)
        except Team.DoesNotExist:
            return None

    def resolve_teams(root, info):
        return Team.objects.all()

class CreateTeamMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        manager_id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    team = graphene.Field(TeamType)

    @classmethod
    def mutate(cls, root, info, name, manager_id):
        team = Team.objects.create(name=name, manager_id=manager_id)
        # Notice we return an instance of this mutation
        return CreateTeamMutation(team=team)

class DeleteTeamMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            team = Team.objects.get(pk=id)
            team.delete()
        except Team.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteTeamMutation(deleted=deleted)
    

class Mutation(graphene.ObjectType):
    create_team = CreateTeamMutation.Field()
    delete_team = DeleteTeamMutation.Field()
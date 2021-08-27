from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene

from .models import UserProfile

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile

class Query(graphene.ObjectType):
    user_profile = graphene.Field(UserProfileType,
                                  id=graphene.ID(required=True))
    user_profiles = graphene.List(UserProfileType)

    def resolve_user_profile(root, info, id):
        try:
            return UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return None

    def resolve_user_profiles(root, info):
        return UserProfile.objects.all()

class CreateUserProfileMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        user_id = graphene.ID(required=True)
        team_id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    user_profile = graphene.Field(UserProfileType)

    @classmethod
    def mutate(cls, root, info, user_id, team_id):
        user_profile = UserProfile.objects.create(user_id=user_id, team_id=team_id)
        # Notice we return an instance of this mutation
        return CreateUserProfileMutation(user_profile=user_profile)

class DeleteUserProfileMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            user_profile = UserProfile.objects.get(pk=id)
            user_profile.delete()
        except UserProfile.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteUserProfileMutation(deleted=deleted)

class UpdateUserProfileMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)
        team_id = graphene.ID(required=True)

    
    user_profile = graphene.Field(UserProfileType)

    @classmethod
    def mutate(cls, root, info, id,user_id, team_id):
        user_profile = UserProfile.objects.get(pk=id)
        user_profile.user_id = user_id
        user_profile.team_id = team_id
        


        user_profile.save()
        # Notice we return an instance of this mutation
        return UpdateUserProfileMutation(user_profile=user_profile)

class Mutation(graphene.ObjectType):
    create_user_profile = CreateUserProfileMutation.Field()
    delete_user_profile = DeleteUserProfileMutation.Field()
    update_user_profile = UpdateUserProfileMutation.Field()
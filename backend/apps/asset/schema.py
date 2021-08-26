from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Asset


class AssetType(DjangoObjectType):
    class Meta:
        model = Asset


class Query(graphene.ObjectType):
    asset = graphene.Field(AssetType,id=graphene.ID(required=True))
    assets = graphene.List(AssetType)

    def resolve_asset(root, info, id):
        try:
            return Asset.objects.get(id=id)
        except Asset.DoesNotExist:
            return None

    def resolve_assets(root, info):
        return Asset.objects.all()


class CreateAssetMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.Text(required=True)
        picture = graphene.Text(required=True)
        cost = graphene.Float(required=True)
        suplier = graphene
        team = graphene


    # The class attributes define the response of the mutation
    asset = graphene.Field(AssetType)

    @classmethod
    def mutate(cls, root, info, name, description, picture, cost, supplier, team):
        asset = Asset.objects.create(name=name, description=description, picture=picture, cost=cost, supplier=supplier, team=team)
        # Notice we return an instance of this mutation
        return CreateAssetMutation(asset=asset)


class DeleteAssetMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            asset = Asset.objects.get(pk=id)
            asset.delete()
        except Asset.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteAssetMutation(deleted=deleted)


class Mutation(graphene.ObjectType):
    create_asset = CreateAssetMutation.Field()
    delete_asset = DeleteAssetMutation.Field()
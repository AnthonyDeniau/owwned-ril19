from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Asset
from ..supplier.schema import SupplierType
# from ..team.schema import TeamType


class AssetType(DjangoObjectType):
    class Meta:
        model = Asset
        fields = "__all__"

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
        description = graphene.String(required=True)
        picture = graphene.String(required=True)
        cost = graphene.Float(required=True)
        suplier = graphene.Field(SupplierType)
        # team = graphene.Field(TeamType)


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

class UpdateAssetMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        picture = graphene.String(required=True)
        cost = graphene.Float(required=True)
        suplier = graphene.Field(SupplierType)
        # team = graphene.Field(TeamType)
    
    asset = graphene.Field(AssetType)

    @classmethod
    def mutate(cls, root, info, id, name, description, picture, cost, supplier, team):
        asset = Asset.objects.get(pk=id)
        asset.name = name
        asset.description = description
        asset.picture = picture
        asset.cost = cost
        asset.supplier = supplier
        asset.team = team
        asset.save()
        # Notice we return an instance of this mutation
        return UpdateAssetMutation(asset=asset)




class Mutation(graphene.ObjectType):
    create_asset = CreateAssetMutation.Field()
    update_asset = UpdateAssetMutation.Field()
    delete_asset = DeleteAssetMutation.Field()


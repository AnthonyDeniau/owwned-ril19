from typing_extensions import Required
from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Inventory, InventoryItem, InventorySession


class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory

class Query(graphene.ObjectType):
    inventory = graphene.Field(InventoryType,
                                  id=graphene.ID(required=True))
    inventorys = graphene.List(InventoryType)

    def resolve_inventory(root, info, id):
        try:
            return InventoryType.objects.get(id=id)
        except InventoryType.DoesNotExist:
            return None

    def resolve_inventorys(root, info):
        return InventoryType.objects.all()

class CreateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        invetory_session = InventorySession(required=True)
        inventory_item = InventoryItem(required=True)

    # The class attributes define the response of the mutation
    inventory = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, invetory_session, inventory_item):
        inventory = Inventory.objects.create(invetory_session=invetory_session, inventory_item=inventory_item)
        # Notice we return an instance of this mutation
        return CreateInventoryMutation(inventory=inventory)

class DeleteInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            inventory = Inventory.objects.get(pk=id)
            inventory.delete()
        except Inventory.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteInventoryMutation(deleted=deleted)

class Mutation(graphene.ObjectType):
    create_organization = CreateInventoryMutation.Field()
    delete_organization = DeleteInventoryMutation.Field()

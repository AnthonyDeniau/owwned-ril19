from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Inventory, InventoryItem, InventorySession


class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory

class Query(graphene.ObjectType):
    inventory = graphene.Field(InventoryType,id=graphene.ID(required=True))
    inventories = graphene.List(InventoryType)

    def resolve_inventory(root, info, id):
        try:
            return Inventory.objects.get(id=id)
        except Inventory.DoesNotExist:
            return None

    def resolve_inventories(root, info):
        return Inventory.objects.all()

class CreateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        invetory_session_id = graphene.ID(required=True)
        inventory_item_id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    inventory = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, invetory_session_id, inventory_item_id):
        inventory = Inventory.objects.create(invetory_session_id=invetory_session_id, inventory_item_id=inventory_item_id)
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



class UpdateInventoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation

        invetory_session_id = graphene.ID(required=True)
        inventory_item_id = graphene.ID(required=True)
        id = graphene.ID()
    
    inventory = graphene.Field(InventoryType)

    @classmethod
    def mutate(cls, root, info, id, invetory_session_id, inventory_item_id):
        inventory = Inventory.objects.get(pk=id)
        inventory.invetory_session_id = invetory_session_id
        inventory.inventory_item_id = inventory_item_id
        inventory.save()
        # Notice we return an instance of this mutation
        return UpdateInventoryMutation(inventory=inventory)

class Mutation(graphene.ObjectType):
    create_inventory = CreateInventoryMutation.Field()
    delete_inventory = DeleteInventoryMutation.Field()
    update_inventory = UpdateInventoryMutation.Field()

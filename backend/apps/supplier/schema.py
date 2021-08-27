from graphene.types import interface
from graphene_django import DjangoObjectType
import graphene
from .models import Supplier


class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier


class Query(graphene.ObjectType):
    supplier = graphene.Field(SupplierType, id=graphene.ID(required=True))
    suppliers = graphene.List(SupplierType)

    def resolve_supplier(root, info, id):
        try:
            return Supplier.objects.get(id=id)
        except Supplier.DoesNotExist:
            return None

    def resolve_suppliers(root, info):
        return Supplier.objects.all()


class CreateSupplierMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        website = graphene.String(required=True)
        login = graphene.String(required=True)
        password = graphene.String(required=True)

    # The class attributes define the response of the mutation
    supplier = graphene.Field(SupplierType)

    @classmethod
    def mutate(cls, root, info, name, website, login, password):
        supplier = Supplier.objects.create(name=name,
                                           website=website,
                                           login=login,
                                           password=password)
        # Notice we return an instance of this mutation
        return CreateSupplierMutation(supplier=supplier)


class DeleteSupplierMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            supplier = Supplier.objects.get(pk=id)
            supplier.delete()
        except Supplier.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteSupplierMutation(deleted=deleted)

class UpdateSupplierMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=False)
        website = graphene.String(required=False)
        login = graphene.String(required=False)
        password = graphene.String(required=False)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    supplier = graphene.Field(SupplierType)

    @classmethod
    def mutate(cls, root, info, id, name, website, login, password):
        supplier = Supplier.objects.get(pk=id)
        supplier.name = name
        supplier.website = website
        supplier.login = login
        supplier.password = password
        supplier.save()
        # Notice we return an instance of this mutation
        return UpdateSupplierMutation(supplier=supplier)


class Mutation(graphene.ObjectType):
    create_supplier = CreateSupplierMutation.Field()
    update_supplier = UpdateSupplierMutation.Field()
    delete_supplier = DeleteSupplierMutation.Field()
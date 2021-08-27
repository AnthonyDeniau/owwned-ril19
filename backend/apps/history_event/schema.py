from graphene_django import DjangoObjectType
import graphene

from .models import EventType, HistoryEvent


class HistoryEventType(DjangoObjectType):
    class Meta:
        model = HistoryEvent
        fields = "__all__"


class Query(graphene.ObjectType):
    history_event = graphene.Field(
        HistoryEventType, id=graphene.ID(required=True))
    history_events = graphene.List(HistoryEventType)

    def resolve_history_event(root, info, id):
        try:
            return HistoryEvent.objects.get(id=id)
        except HistoryEvent.DoesNotExist:
            return None

    def resolve_history_events(root, info):
        return HistoryEvent.objects.all()


class CreateHistoryEventMutation(graphene.Mutation):
    class Arguments:
        stakeholder_id = graphene.ID(required=False)
        asset_id = graphene.ID(required=True)
        start_date = graphene.DateTime(required=True)
        end_date = graphene.DateTime(required=False)
        description = graphene.String(required=False)
        event_type = graphene.String(required=True)

    # The class attributes define the response of the mutation
    history_event = graphene.Field(HistoryEventType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        history_event = HistoryEvent.objects.create(**kwargs)
        # Notice we return an instance of this mutation
        return CreateHistoryEventMutation(history_event=history_event)


class DeleteHistoryEventMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    deleted = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleted = True
        try:
            history_event = HistoryEvent.objects.get(pk=id)
            history_event.delete()
        except HistoryEvent.DoesNotExist:
            deleted = False
        # Notice we return an instance of this mutation
        return DeleteHistoryEventMutation(deleted=deleted)


class UpdateHistoryEventMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        stakeholder_id = graphene.ID(required=False)
        asset_id = graphene.ID(required=False)
        start_date = graphene.DateTime(required=False)
        end_date = graphene.DateTime(required=False)
        description = graphene.String(required=False)
        event_type = graphene.String(required=False)

    history_event = graphene.Field(HistoryEventType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        history_event = HistoryEvent.objects.get(pk=id)
        for attr, value in kwargs.items():
            setattr(history_event, attr, value)
        history_event.save()
        # Notice we return an instance of this mutation
        return UpdateHistoryEventMutation(history_event=history_event)


class Mutation(graphene.ObjectType):
    create_history_event = CreateHistoryEventMutation.Field()
    update_history_event = UpdateHistoryEventMutation.Field()
    delete_history_event = DeleteHistoryEventMutation.Field()

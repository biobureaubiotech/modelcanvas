from django.db import models
from colorfield.fields import ColorField
from ordered_model.models import OrderedModel


ITEM_TYPE = (
    ('BL', 'Backlog' ),
    ('KP', 'Key Partners'),
    ('KA', 'Key Activities'),
    ('VP', 'Value Propositions'),
    ('CR', 'Customer Relationships'),
    ('KR', 'Key Resources'),
    ('CH', 'Channels'),
    ('CS', 'Cost Structure'),
    ('RS', 'Revenue Streams'),
)

class Canvas(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)

class CanvasItem(OrderedModel):
    canvas = models.ForeignKey('Canvas', related_name="items")
    color = ColorField()
    itemtype = models.CharField(max_length=2, default='BL', choices=ITEM_TYPE)
    title = models.CharField(max_length=25)
    description = models.TextField()

    class Meta(OrderedModel.Meta):
        pass


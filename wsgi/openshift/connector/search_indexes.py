import datetime
from haystack import indexes
from connector.models import *


class SkillIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    member = indexes.CharField(model_attr='member')
    category = indexes.CharField(model_attr='category', faceted=True)

    def get_model(self):
        return Skill

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class OfferIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    member = indexes.CharField(model_attr='member')
    category = indexes.CharField(model_attr='category', faceted=True)
    organization = indexes.CharField(model_attr='organization')

    def get_model(self):
        return Offer

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
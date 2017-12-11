from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex

class PoliticianIndex(AlgoliaIndex):
    index_name = 'politicians'

class CommitteeIndex(AlgoliaIndex):
    index_name = 'committees'

class BillIndex(AlgoliaIndex):
    index_name = 'bills'

class PolitifindConfig(AppConfig):
    name = 'politifind'

    def ready(self):

        Politician = self.get_model('politician')
        Committee = self.get_model('committee')
        Bill = self.get_model('bill')

        algoliasearch.register(Politician, PoliticianIndex)
        algoliasearch.register(Committee, CommitteeIndex)
        algoliasearch.register(Bill, BillIndex)

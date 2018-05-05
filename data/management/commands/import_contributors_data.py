import requests
import logging

from data.models import Contributor
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://webservices.coala.io/contrib/'


class Command(BaseCommand):
    def import_data(self, contributor):
        login = contributor.get('login', None)
        name = contributor.get('name', None)
        bio = contributor.get('bio', None)
        num_commits = contributor.get('contributions', None)
        issues_opened = contributor.get('issues', None)
        reviews = contributor.get('reviews', None)

        logger = logging.getLogger(__name__)
        try:
            c, created = Contributor.objects.get_or_create(
                login=login,
                name=name,
                bio=bio,
                num_commits=num_commits,
                issues_opened=issues_opened,
                reviews=reviews
            )
            if created:
                c.save()
                logger.info('\nContributor, %s has been saved.' % c)
        except Exception as ex:
            logger.error(
                '\n\nSomething went wrong saving this contributor %s: %s'
                % (login, ex))

    def handle(self, *args, **options):
        """
        Makes a GET request to the  API.
        """
        logger = logging.getLogger(__name__)
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.get(
                url=IMPORT_URL,
                headers=headers,
            )
            response.raise_for_status()
        except Exception as e:
            logger.error(e)
            return

        data = response.json()

        for contributor in data:
            self.import_data(contributor)

from django.core.management.base import BaseCommand
import requests
from myapp.models import Post
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetches multiple quotes and saves them as Posts.'

    def handle(self, *args, **kwargs):
        url = ''
        response = requests.get(url)
        quotes = response.json()

        saved_count = 0
        for quote in quotes[:10]:  # Save only 10 quotes max (optional)
            title = quote.get('text', '').strip()
            description = quote.get('author', 'Unknown')

            if title and not Post.objects.filter(title=title).exists():
                Post.objects.create(
                    title=title,
                    description=description,
                    published_date=datetime.now()
                )
                saved_count += 1

        self.stdout.write(self.style.SUCCESS(f"{saved_count} quotes saved successfully."))

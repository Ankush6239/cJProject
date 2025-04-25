from django.core.management.base import BaseCommand
import requests
from myapp.models import Post
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetches multiple quotes and saves them as Posts.'

    def handle(self, *args, **kwargs):
        url = 'https://type.fit/api/quotes'  # ✅ Public quotes API

        try:
            response = requests.get(url)
            response.raise_for_status()
            quotes = response.json()
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f"API request failed: {e}"))
            return

        saved_count = 0
        for quote in quotes[:10]:  # Save only 10 quotes max
            title = quote.get('text', '').strip()
            description = quote.get('author') or 'Unknown'

            if title and not Post.objects.filter(title=title).exists():
                Post.objects.create(
                    title=title,
                    description=description,
                    published_date=datetime.now()
                )
                saved_count += 1

        self.stdout.write(self.style.SUCCESS(f"{saved_count} quotes saved successfully."))

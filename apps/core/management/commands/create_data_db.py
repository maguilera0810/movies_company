from django.core.management.base import BaseCommand
from apps.


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('amount_days', type=int, help='Cuantos textos se quiere crears')
        parser.add_argument('until_day', type=int, help='Hasta que texto se quiere crear')

    def handle(self, *args, **kwargs):
        print('------------------- START --------------------------')
        filters = {"type": StreakTextType.COUNT_STORY.value}
        for s in StreakRepository().get_streak_texts():
            print(s)
        last_day = 0
        if streak_text := StreakRepository().get_streak_texts().filter(**filters).order_by('-day').first():
            last_day = streak_text.day
        amount_days = kwargs.get('amount_days')
        until_day = kwargs.get('until_day')
        if not amount_days:
            amount_days = until_day - last_day
        for idx, day in enumerate(range(last_day + 1 , last_day + amount_days + 1), start=1):
            print(f"- {idx} -----------{day=}")
            data = {"day": day,
                    "type": StreakTextType.COUNT_STORY.value,
                    }
            serializer = StreakTextSerializer(
                data=data, partial=True)
            if serializer.is_valid():
                streak_text = serializer.save()
                title_lokalise_key_id, description_lokalise_key_id = StreakService().create_streak_text_lokalise_keys(
                    streak_text, 'en')
                if title_lokalise_key_id:
                    streak_text.title_lokalise_key_id = title_lokalise_key_id
                if description_lokalise_key_id:
                    streak_text.description_lokalise_key_id = description_lokalise_key_id
                streak_text.save()

        print('-------------------- END ---------------------------')
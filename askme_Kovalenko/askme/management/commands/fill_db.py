from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from forum.models import Question, Answer, Tag, Rating
from random import choice, randint

# python manage.py filldata 500

class Command(BaseCommand):
    help = 'Fill db with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Ratio for test data')

    def handle(self, *args, **options):
        ratio = options['ratio']
        num_users = ratio
        num_questions = ratio * 10
        num_answers = ratio * 100
        num_tags = ratio
        num_ratings = ratio * 200

        # Create users
        for i in range(num_users):
            User.objects.create_user(
                username=f'user{i}',
                password='password'
            )

        # Create tags
        for i in range(num_tags):
            Tag.objects.create(
                name=f'Tag{i}'
            )

        users = User.objects.all()
        tags = Tag.objects.all()

        # Create questions
        for i in range(num_questions):
            question = Question.objects.create(
                author=choice(users),
                title=f'Title{i}',
                text=f'Text{i}'
            )
            for j in range(randint(1, 5)):
                question.tags.add(choice(tags))

        questions = Question.objects.all()

        # Create answers
        for i in range(num_answers):
            Answer.objects.create(
                author=choice(users),
                question=choice(questions),
                text=f'Text{i}'
            )

        answers = Answer.objects.all()

        # Create ratings
        for i in range(num_ratings):
            rating = choice([-1, 1])
            Rating.objects.create(
                user=choice(users),
                question=choice(questions),
                answer=choice(answers),
                rating=rating
            )

        self.stdout.write(f'Successfully filled db with test data. Ratio: {ratio}')
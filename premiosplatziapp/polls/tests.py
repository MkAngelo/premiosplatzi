import datetime

from django.utils import timezone
from django.urls.base import reverse
from django.test import TestCase

from .models import Question

# Testeas:
#   Modelos
#   Vistas
class QuestionModelTests(TestCase):
	# Bateria de tests
	def test_was_published_recently_with_future_questions(self):
		"""was_published_recently returns False for questions whose pub_date is in the future"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(question_text="Quien es el mejor Course Director de Platzi?",pub_date=time)

		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_present_questions(self):
		"""was_published_recently returns True for questions whose pub_date is in the present"""
		time = timezone.now()
		present_question = Question(question_text="Quien es el mejor Course Director de Platzi?",pub_date=time)

		self.assertIs(present_question.was_published_recently(), True)

	def test_was_published_recently_with_past_questions(self):
		"""was_published_recently returns False for questions whose pub_date is in the present"""
		time = timezone.now() - datetime.timedelta(days=30)
		past_question = Question(question_text="Quien es el mejor Course Director de Platzi?",pub_date=time)

		self.assertIs(past_question.was_published_recently(), False)

class QuestionIndexViewTests(TestCase):
	def test_no_questions(self):
		"""If no question exist, an appropiate message is displayed"""
		response = self.client.get(reverse("polls:index"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context["latest_question_list"],[])

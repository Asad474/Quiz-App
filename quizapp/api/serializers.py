from rest_framework.serializers import ModelSerializer
from quizapp.models import *


class TopicSerailizer(ModelSerializer):
    class Meta:
        model = Quiztopic
        fields = '__all__'


class SubTopicSerailizer(ModelSerializer):
    class Meta:
        model = Subtopic
        fields = '__all__'


class QuizquestionSerailizer(ModelSerializer):
    class Meta:
        model = Quizquestion
        fields = '__all__'
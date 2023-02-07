from rest_framework.response import Response
from rest_framework.decorators import api_view
from quizapp.models import * 
from .serializers import *


@api_view(['GET'])
def apioverview(request):
    routes = [ 
        'GET /api/',
        'GET /api/topics/',
        'GET /api/topics/:id',
        'GET /api/questions/',
        'GET /api/questions/:id',
        'GET /api/subtopics/questions/:id',
    ]

    return Response(routes)


@api_view(['GET'])
def quiztopics(request):
    topics = Quiztopic.objects.all()
    topics_serializer = TopicSerailizer(topics, many = True)
    return Response(topics_serializer.data)


@api_view(['GET'])
def quizsubtopics(request, pk):
    topic = Quiztopic.objects.get(id = pk)
    sub_topics = topic.subtopic_set.all()
    sub_topics_serializer = SubTopicSerailizer(sub_topics, many = True)
    return Response(sub_topics_serializer.data)


@api_view(['GET'])
def quizquestions(request):
    questions = Quizquestion.objects.all()
    questions_serializer = QuizquestionSerailizer(questions, many = True)
    return Response(questions_serializer.data)


@api_view(['GET'])
def quiztopicquestions(request, pk):
    topic = Quiztopic.objects.get(id = pk)
    questions = topic.quizquestion_set.all()
    questions_serializer = QuizquestionSerailizer(questions, many = True)
    return Response(questions_serializer.data)


@api_view(['GET'])
def quizsubtopicquestions(request, pk):
    sub_topic = Subtopic.objects.get(id = pk)
    questions = sub_topic.quizquestion_set.all()
    questions_serializer = QuizquestionSerailizer(questions, many = True)
    return Response(questions_serializer.data)
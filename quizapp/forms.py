from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : TextInput(attrs = {'placeholder' : 'Enter Username', 'class' : 'form-control form-control-lg'}),
            'email' : EmailInput(attrs = {'placeholder' : 'Enter Email', 'class' : 'form-control form-control-lg'}),
        }

    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs = {'placeholder' : 'Enter Password', 'class' : 'form-control form-control-lg'})
        self.fields['password2'].widget = PasswordInput(attrs = {'placeholder' : 'Enter Confirm Password', 'class' : 'form-control form-control-lg'})


class QuestionForm(ModelForm):
    class Meta:
        model = Quizquestion 
        fields = '__all__'
        widgets = { 
            'topic_name' : Select(attrs = {'class' : 'form-control form-control-lg'}),
            'sub_topic_name' : Select(attrs = {'class' : 'form-control form-control-lg'}),
            'question' : Textarea(attrs = {'placeholder' : 'Enter Question', 'class' : 'form-control form-control-lg'}),
            'option_1' : TextInput(attrs = {'placeholder' : 'Enter Option1', 'class' : 'form-control form-control-lg'}),
            'option_2' : TextInput(attrs = {'placeholder' : 'Enter Option2', 'class' : 'form-control form-control-lg'}),
            'option_3' : TextInput(attrs = {'placeholder' : 'Enter Option3', 'class' : 'form-control form-control-lg'}),
            'option_4' : TextInput(attrs = {'placeholder' : 'Enter Option4', 'class' : 'form-control form-control-lg'}),
            'correct_answer' : TextInput(attrs = {'placeholder' : 'Enter Correct answer', 'class' : 'form-control form-control-lg'}),
        }


class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'avatar']
        widgets = {
            'username' : TextInput(attrs = {'placeholder' : 'Enter Username', 'class' : "form-control form-control-lg"}),
            'bio' : Textarea(attrs = {'placeholder' : 'Enter about yourself', 'class' : 'form-control form-control-lg'}),
        }
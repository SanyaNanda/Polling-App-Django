from django import forms
from .models import Question, Choice


class QuesForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question_text',)
		
		# widgets = {
		# 	'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title of the blog here'}),
		# 	'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'sanya', 'type':'hidden'}),
		# }

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ('choice_text',)

		# widgets = {
		# 	'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title of the blog here'}),
		# 	'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing your blog'}),
		# }
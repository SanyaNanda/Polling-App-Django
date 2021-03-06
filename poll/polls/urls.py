from django.urls import path
from . import views

app_name= 'polls'

# urlpatterns = [
# 	# ex: /polls/
# 	path('', views.index, name='index'),
# 	# ex: /polls/5/
# 	path('<int:question_id>/', views.detail, name='detail'),
# 	# ex: /polls/5/results/
# 	path('<int:question_id>/results/', views.results, name='results'),
# 	# ex: /polls/5/vote/
# 	path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('create/', views.QuesView.as_view(), name='ques'),
	path('search/', views.search, name='search'),
	path('<int:pk>/option/', views.ChoiceView.as_view(), name='option'),
	path('<int:pk>/choice/', views.choice, name='choice'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:pk>/voted/', views.VotedView.as_view(), name='voted'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('<str:obj>/resultdata/', views.resultData, name='resultdata'),
]
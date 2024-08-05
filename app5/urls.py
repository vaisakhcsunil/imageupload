from .import views
from django.urls import path
# from .views import studentcreate
# from .views import studentList
# from .views import studentDetailView
# from .views import studentupdateView
# from .views import studentDeleteView


# urlpatterns=[
#     path("",studentcreate.as_view()),
#     path("list/",studentList.as_view()),
#     path('<pk>/',studentDetailView.as_view()),
#     path('<pk>/update',studentupdateView.as_view()),
#     path('<pk>/delete/',studentDeleteView.as_view()),

# ]
urlpatterns=[
    path('upload/',views.upload,name='upload'),
]
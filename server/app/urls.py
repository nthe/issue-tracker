from django.urls import path
import app.views as views

urlpatterns = [
    path('category', views.CategoryListView.as_view()),
    path('category/<int:pk>', views.CategoryCreateEditView.as_view()),
    path('status', views.StatusListView.as_view()),
    path('status/<int:pk>', views.StatusCreateEditView.as_view()),
    path('issue', views.IssueListView.as_view()),
    path('issue/<int:pk>', views.IssueCreateEditView.as_view()),
]

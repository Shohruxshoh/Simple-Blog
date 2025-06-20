from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, \
    CommentListCreateAPIView, CommentDeleteView

urlpatterns = [
    path('', PostListView.as_view()),
    path('create', PostCreateView.as_view()),
    path('update/<int:pk>', PostUpdateView.as_view()),
    path('detail/<int:pk>', PostDetailView.as_view()),
    path('delete/<int:pk>', PostDeleteView.as_view()),

    path('<int:post_id>/comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>', CommentDeleteView.as_view())
]

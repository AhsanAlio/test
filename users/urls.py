from django.urls import include, path
from django.conf.urls import url
from users import views


urlpatterns = [
    # path('accounts/', include('users.urls')),
    url ('test/', views.TestView.as_view()),
    path('api/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url ('register/', views.RegisterView.as_view()),
    url ('user/', views.UserView.as_view()),
    url ('stockfish/',views.stockfish_best_move.as_view()),
    path('googleLogin/',views.home),
    url ('predictMove/',views.PredictMove.as_view()),

]

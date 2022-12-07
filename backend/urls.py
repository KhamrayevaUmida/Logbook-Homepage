from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', AboutView.as_view()),
    path('author/', AuthorView.as_view()),
    path('contact/', ContactView.as_view()),
    path('full-left/', FullleftView.as_view()),
    path('full-right/', FullrightView.as_view()),
    path('full/', FullView.as_view()),
    path('list-right/', ListrightView.as_view()),
    path('list-left/', ListleftView.as_view()),
    path('list', ListView.as_view()),
    path('post-details-1/', Postd1View.as_view()),
    path('post-details-2/', Postd2View.as_view()),
    path('post-elements/', PostelementsView.as_view()),
    path('privacy-policy/', PrivacyView.as_view()),
    path('terms-conditions/', TermsView.as_view()),
]

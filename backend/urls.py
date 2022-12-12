from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', AboutView.as_view(), name="about"),
    path('author/', AuthorView.as_view(), name="author"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('full-left/', FullleftView.as_view(), name="full-l"),
    path('full-right/', FullrightView.as_view(), name="full-r"),
    path('full/', FullView.as_view(), name="full"),
    path('list-right/', ListrightView.as_view(), name="list-r"),
    path('list-left/', ListleftView.as_view(), name="list-l"),
    path('list/', ListView.as_view(), name="list"),
    path('post-details-1/', Postd1View.as_view(), name="post-d1"),
    path('post-details-2/', Postd2View.as_view(), name="post-d2"),
    path('post-elements/', PostelementsView.as_view(), name="post-el"),
    path('privacy-policy/', PrivacyView.as_view(), name="privacy"),
    path('terms-conditions/', TermsView.as_view(), name="terms"),
]

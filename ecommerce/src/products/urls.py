from django.conf.urls import url,include
from .views import ProductListView,ProductDetailSlugView

urlpatterns = [
    url((r'^$'),ProductListView.as_view() ),
    url((r'^(?P<slug>[\w-]+)/$'), ProductDetailSlugView.as_view()),

]
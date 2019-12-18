from django.conf.urls import url

# App imports
from .views import hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'locatio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello)
]

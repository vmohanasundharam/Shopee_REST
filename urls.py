from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^api/auntheticate/(?P<uname>[\w.@+-]+)/(?P<passwd>[\w.@+-]+)/$', views.authenticateuser, name='authenticateuser'),
	url(r'^api/pid/(?P<id>[\w.@+-]+)/$', views.product_id, name='product_id'),
	url(r'^api/pname/(?P<name>[\w.@+-]+)/$', views.product_name, name='product_name'),
	url(r'^api/pcat/(?P<category>[\w.@+-]+)/$', views.product_category, name='product_category'),
	url(r'^api/post/(?P<id>[\w.@+-]+)/(?P<name>[\w.@+-]+)/(?P<category>[\w.@+-]+)/(?P<price>[\w.@+-]+)/$', views.feed_product, name='feed_product'),
	url(r'^api/put/(?P<id>[\w.@+-]+)/(?P<name>[\w.@+-]+)/(?P<category>[\w.@+-]+)/(?P<price>[\w.@+-]+)/$', views.feed_product, name='feed_product'),
]

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from myfeeds.models import Feed


class IndexView(generic.ListView):
    template_name = 'myfeeds/index.html'

    def get_queryset(self):
        return Feed.objects


class FeedDetailView(generic.DetailView):
    model = Feed
    template_name = 'myfeeds/feed.html'


class FeedView(generic.DetailView):
    model = Feed
    content_type = 'application/rss+xml; charset=utf-8'
    template_name = 'myfeeds/rss.xml'


# Shows feeds
def index(req):
    return HttpResponse("Hello, you should later see feed names here.")


def feed(req, feed_id):
    return HttpResponse("This is feed %s" % feed_id)

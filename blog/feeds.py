"""Generates a feed of the latest posts for the blog."""

import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    """Generates a feed of the latest posts for the blog.

This class creates a feed for the latest posts of the blog and includes methods to retrieve the latest posts, 
their titles, descriptions, and publication dates.

Attributes:
    title (str): The title of the blog feed.
    link (str): The link to the blog's post list.
    description (str): The description of the new posts for the blog.

Methods:
    items(self): Retrieves the latest published posts for the feed.
    item_title(self, item): Returns the title of the specified post item.
    item_description(self, item): Returns the truncated HTML content of the specified post item's body.
    item_pubdate(self, item): Returns the publication date of the specified post item.
"""

    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish

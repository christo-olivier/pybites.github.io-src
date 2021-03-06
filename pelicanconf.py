#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pybites'
SITENAME = 'PyBites'
SITETITLE = 'PyBites'
SITESUBTITLE = u'We Create Rockstar Python Developers'
SITEDESCRIPTION = SITESUBTITLE
SITEURL = 'https://pybit.es'
SITELOGO = 'https://pybit.es/theme/img/profile.png'
# local testing / document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'
THEME = 'nest'
PYGMENTS_STYLE = 'github'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = 'feeds/all.rss.xml'  # this is the constant used in flex
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
INDEX_SAVE_AS = 'blog_index.html'

TWITTER_USERNAME = "pybites"
GITHUB_USERNAME = "pybites"

DEFAULT_PAGINATION = 10

ADD_THIS_ID = 'ra-5859c6a67eb6254d'
DISQUS_SITENAME = 'http-pybit-es'
GOOGLE_ANALYTICS = 'UA-89294245-1'
CC_ES = False

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico',
    'extra/logo.png',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.png': {'path': 'logo.png'}
}
FAVICON = 'favicon.ico'

# embed jupyter notebooks and post stats
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'post_stats', 'i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']

NEST_HEADER_IMAGES = 'circuit-bg.png'
NEST_HEADER_LOGO = '/images/logo.png'


NEST_CSS_MINIFY = True

MENUITEMS = [
    ('Home', '/'),
    ('Blog', '/archives.html'),
    ('Platform','https://codechalleng.es'),
    ('Apply','/pages/apply.html')
]

NEST_ARCHIVES_HEADER_TITLE = 'Archive'

# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [
    ('Community', '/pages/community.html'),
    ('#100DaysOfCode', 'https://training.talkpython.fm/courses/explore_100days_web/100-days-of-web-in-python'),
    ('Search', '/pages/search.html'),
    ('Privacy', '/pages/privacy-policy.html'),
]

NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_COPYRIGHT = u'&copy; PyBites 2016+'
# Footer optional
NEST_FOOTER_HTML = ''

NEST_LINKS_COLUMN_TITLE = u'Reach Out'
LINKS = (
    ('Email', 'mailto:info@pybit.es'),
    ('Twitter', 'https://twitter.com/pybites'),
    ('Facebook','https://facebook.com/pybites'),
    ('Github','https://github.com/pybites'),
    ('Open Source','https://github.com/PyBites-Open-Source'),
    ('YouTube','https://www.youtube.com/channel/UCBn-uKDGsRBfcB0lQeOB_gA'),
)

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/', 'views': 130},
        {'title': 'How to Think Like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/', 'views': 100},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 120},
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views': 140},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/', 'views': 110},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 150},
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/', 'views': 170},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org', 'views': 140},
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p, created = Page.objects.get_or_create(category=cat, title=title, defaults={'url': url, 'views': views})
    if created:
        p.url = url
        p.views = views
        p.save()
    return p

def add_cat(name, views = 0, likes = 0):
    c, created = Category.objects.get_or_create(name=name, defaults={'views': views, 'likes': likes})
    if created:
        c.views = views
        c.likes = likes
        c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
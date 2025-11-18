#!/usr/bin/env python
import os
import sys
import django
from django.core.management import execute_from_command_line
from django.test import Client
from django.urls import reverse
import shutil

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

# Create dist directory
if os.path.exists('dist'):
    shutil.rmtree('dist')
os.makedirs('dist')

# Install dependencies and collect static files
os.system('pip install -r requirements.txt')
execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])

# Copy static files to dist
if os.path.exists('staticfiles'):
    shutil.copytree('staticfiles', 'dist/static')

# Generate static HTML files
client = Client()

# Define your URLs and their output filenames
urls = {
    '/': 'index.html',
    '/about/': 'about.html', 
    '/projects/': 'projects.html',
    '/contact/': 'contact.html',
    '/projects/kgl-inventory/': 'project1.html',
    '/projects/ecommerce-site/': 'project2.html',
    '/projects/portfolio/': 'project3.html',
}

print("Generating static HTML files...")
for url, filename in urls.items():
    try:
        response = client.get(url)
        if response.status_code == 200:
            with open(f'dist/{filename}', 'w', encoding='utf-8') as f:
                f.write(response.content.decode('utf-8'))
            print(f"Generated {filename}")
        else:
            print(f"Error generating {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"Error generating {filename}: {e}")

print("Static site generation complete!")
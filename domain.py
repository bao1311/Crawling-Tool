from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get PROJECTNAME based on the url
def get_project_name(url):
    try:
        lst = url.split('.')
        name = lst[0]
        if 'https' in name:
            return name[8:]
        return name[7:]
    except:
        return ''

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

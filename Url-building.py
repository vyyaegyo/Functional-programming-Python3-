def url(scheme, domain, path):
    return f'{scheme}://{domain}/{path}'

def url_curried(scheme):
    def inner(domain):
        def inner2(path):
            return url(scheme, domain, path)
        return inner2
    return inner

http = url_curried('http')
some_website = http('some-website,com')


url_1 = some_website('photos/photos1') 
url_2 = some_website('photos/photos2') 
url_3 = some_website('photos/photos3') 
url_4 = some_website('photos/photos4') 
url_5 = some_website('photos/photos5') 

print(url_1)
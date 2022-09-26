# Write a function that when given a URL as a string, parses out just 
# the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

#given url as string
#get past https://
#if www. is there get passed that
# get all the text from there to .com

#edge case www.dumbsite.com



url = "www.dumbsite.com"

def get_domain(url):
    if url[0] == 'h':
        url = url.split('/')
    url = url.split('.')
    if url[0] == 'www':
        return url[1]
    else:
        return url[0]
    print(url)

get_domain(url)

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = f'https://github.com/{github_user}'

r = requests.get(url)
soup = bs(r.content, 'html.parser')

# Look for the profile image using a different selector (we'll use the 'avatar' class)
profile_image_tag = soup.find('img', {'class': 'avatar-user'})
if profile_image_tag:
    profile_image = profile_image_tag['src']
    print("Profile Image URL:", profile_image)
else:
    print("Could not find the profile image.")

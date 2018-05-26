from .models import Post,User,Comment,Like,Dislike

def get_details(backend, strategy, details, response, user, *args, **kwargs):
  url = response['image'].get('url')
  User.objects.create(name=user,image=url)

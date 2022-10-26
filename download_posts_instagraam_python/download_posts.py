from datetime import datetime
import instaloader

#carrega a bliblioteca e faz o login no instagram 
drive = instaloader.Instaloader()
#coloque o seu usuário e senha do instagram
drive.login('usuario do seu insta','coloque a senha do seu insta')

#carrega  todos os posts do perfil desejado
posts = instaloader.Profile.from_username(drive.context, "perfil que você deseja baixar os posts ").get_posts()

#periodo que deseja baixar os posts
SINCE = datetime(2022,1,10)
UNTIL = datetime(2022,1,20)

#percorre todos os posts e baixa somente os que estão na data

for post in posts:
    if(post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        drive.download_post(post,"insta_post_downloads")
    
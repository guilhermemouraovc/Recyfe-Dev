from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.apps import apps
from django.conf import settings

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/')
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.username

    def serialize(self):
        return {
            'id': self.id,
            "username": self.username,
            "profile_pic": self.profile_pic.url,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    
class UserCredits(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_credits")
    saldo = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Saldo: {self.saldo} créditos"

class UserReward(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_rewards")
    reward = models.ForeignKey('network.Reward', on_delete=models.CASCADE, related_name="reward_users")
    redeemed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.reward.nome}"

class CreditCode(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    saldo = models.PositiveIntegerField(default=100)
    utilizado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario_usado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {'Usado' if self.utilizado else 'Válido'}"

    def redeem(self, user):
        if not self.utilizado:
            user_credits, _ = UserCredits.objects.get_or_create(user=user)
            user_credits.saldo += self.saldo
            user_credits.save()

            self.utilizado = True
            self.usuario_usado = user
            self.save()
        else:
            raise ValueError("Este código já foi utilizado.")


class Reward(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor_em_creditos = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='recompensas/')

    def __str__(self):
        return f"{self.nome} - {self.valor_em_creditos} créditos"

class Post(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date_created = models.DateTimeField(default=timezone.now)
    content_text = models.TextField(max_length=140, blank=True)
    content_image = models.ImageField(upload_to='posts/', blank=True)
    likers = models.ManyToManyField(User,blank=True , related_name='likes')
    savers = models.ManyToManyField(User,blank=True , related_name='saved')
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Post ID: {self.id} (creater: {self.creater})"

    def img_url(self):
        return self.content_image.url

    def append(self, name, value):
        self.name = value

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenters')
    comment_content = models.TextField(max_length=90)
    comment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post: {self.post} | Commenter: {self.commenter}"

    def serialize(self):
        return {
            "id": self.id,
            "commenter": self.commenter.serialize(),
            "body": self.comment_content,
            "timestamp": self.comment_time.strftime("%b %d %Y, %I:%M %p")
        }
    
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f"User: {self.user}"
    

class MapPoint(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Ponto")
    description = models.TextField(blank=True, verbose_name="Descrição")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    
    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"
    
class Resgate(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Reward, on_delete=models.CASCADE)
    data_resgate = models.DateTimeField(auto_now_add=True)
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from .models import Reward
from .models import Resgate


import json

from .models import User, Post, Comment, Follower, UserCredits, Reward, CreditCode, MapPoint
from ecommerce.pedido.models import Pedido, ItemPedido

    
def index(request):
    all_posts = Post.objects.all().order_by('-date_created')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    posts = paginator.get_page(page_number)
    followings = []
    suggestions = []
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
    return render(request, "network/index.html", {
        "posts": posts,
        "suggestions": suggestions,
        "page": "all_posts",
        'profile': False
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        profile = request.FILES.get("profile")
        print(f"--------------------------Profile: {profile}----------------------------")
        cover = request.FILES.get('cover')
        print(f"--------------------------Cover: {cover}----------------------------")

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            if profile is not None:
                user.profile_pic = profile
            else:
                user.profile_pic = "profile_pic/no_pic.png"
            user.cover = cover           
            user.save()
            Follower.objects.create(user=user)
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def email(request):
    return render(request, 'parciais/_email.html')

def profile(request, username):
    user = User.objects.get(username=username)
    all_posts = Post.objects.filter(creater=user).order_by('-date_created')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    posts = paginator.get_page(page_number)
    followings = []
    suggestions = []
    follower = False
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]

        if request.user in Follower.objects.get(user=user).followers.all():
            follower = True
    
    follower_count = Follower.objects.get(user=user).followers.all().count()
    following_count = Follower.objects.filter(followers=user).count()
    return render(request, 'network/profile.html', {
        "username": user,
        "posts": posts,
        "posts_count": all_posts.count(),
        "suggestions": suggestions,
        "page": "profile",
        "is_follower": follower,
        "follower_count": follower_count,
        "following_count": following_count
    })

def following(request):
    if request.user.is_authenticated:
        following_user = Follower.objects.filter(followers=request.user).values('user')
        all_posts = Post.objects.filter(creater__in=following_user).order_by('-date_created')
        paginator = Paginator(all_posts, 10)
        page_number = request.GET.get('page')
        if page_number == None:
            page_number = 1
        posts = paginator.get_page(page_number)
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
        return render(request, "network/index.html", {
            "posts": posts,
            "suggestions": suggestions,
            "page": "following"
        })
    else:
        return HttpResponseRedirect(reverse('login'))

def saved(request):
    if request.user.is_authenticated:
        all_posts = Post.objects.filter(savers=request.user).order_by('-date_created')

        paginator = Paginator(all_posts, 10)
        page_number = request.GET.get('page')
        if page_number == None:
            page_number = 1
        posts = paginator.get_page(page_number)

        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
        return render(request, "network/index.html", {
            "posts": posts,
            "suggestions": suggestions,
            "page": "saved"
        })
    else:
        return HttpResponseRedirect(reverse('login'))
        
@csrf_exempt
def enviar_email_pedido(request):
    """
    View para processar o envio de email com detalhes do pedido.
    Aceita requisições POST com dados do pedido em JSON.
    """
    if request.method != 'POST':
        return JsonResponse({
            'status': 'erro',
            'mensagem': 'Método inválido.'
        })

    try:
        # Processa os dados da requisição
        dados = json.loads(request.body)
        pedido_id = dados.get('pedido_id')
        total = dados.get('total')
        itens = dados.get('itens', [])
        usuario = request.user

        def limpar_valor(valor):
            """Converte strings de valor monetário para float."""
            return float(valor.replace('R$', '').replace(' ', '').replace(',', '.'))

        # Processa o valor total
        try:
            total = limpar_valor(total)
        except Exception as e:
            return JsonResponse({
                'status': 'erro',
                'mensagem': f'Erro ao processar o total: {str(e)}'
            })

        # Valida a estrutura dos itens
        if not isinstance(itens, list):
            return JsonResponse({
                'status': 'erro',
                'mensagem': 'Itens não são uma lista válida.'
            })

        # Processa cada item do pedido
        for item in itens:
            if not isinstance(item, dict):
                return JsonResponse({
                    'status': 'erro',
                    'mensagem': f'O item {item} não é um dicionário válido.'
                })

            if 'total' not in item:
                return JsonResponse({
                    'status': 'erro',
                    'mensagem': f'O item {item} não contém a chave "total".'
                })

            try:
                item['total'] = limpar_valor(item['total'])
            except Exception as e:
                return JsonResponse({
                    'status': 'erro',
                    'mensagem': f'Erro ao processar item {item.get("produto", "desconhecido")}: {str(e)}'
                })

        # Prepara os dados para o template
        pedido = {
            'id': pedido_id,
            'total': total,
            'usuario': usuario,
        }

        # Renderiza o template do email
        mensagem_html = render_to_string(
            'parciais/_email.html',
            {
                'pedido': pedido,
                'itens': itens
            }
        )

        # Envia o email
        send_mail(
            subject='Detalhes do Pedido',
            message='',  # Corpo em texto simples
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
            fail_silently=False,
            html_message=mensagem_html
        )

        return JsonResponse({
            'status': 'sucesso',
            'mensagem': 'E-mail enviado com sucesso!'
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'erro',
            'mensagem': 'Erro ao processar os dados do pedido. Formato JSON inválido.'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'erro',
            'mensagem': f'Erro inesperado: {str(e)}'
        })

@login_required
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        try:
            post = Post.objects.create(creater=request.user, content_text=text, content_image=pic)
            return HttpResponseRedirect(reverse('index'))
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse("Method must be 'POST'")

@login_required
@csrf_exempt
def edit_post(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('text')
        pic = request.FILES.get('picture')
        img_chg = request.POST.get('img_change')
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        try:
            post.content_text = text
            if img_chg != 'false':
                post.content_image = pic
            post.save()
            
            if(post.content_text):
                post_text = post.content_text
            else:
                post_text = False
            if(post.content_image):
                post_image = post.img_url()
            else:
                post_image = False
            
            return JsonResponse({
                "success": True,
                "text": post_text,
                "picture": post_image
            })
        except Exception as e:
            print('-----------------------------------------------')
            print(e)
            print('-----------------------------------------------')
            return JsonResponse({
                "success": False
            })
    else:
            return HttpResponse("Method must be 'POST'")

@csrf_exempt
def like_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            print(post)
            try:
                post.likers.add(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unlike_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            print(post)
            try:
                post.likers.remove(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def save_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            print(post)
            try:
                post.savers.add(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unsave_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(pk=id)
            print(post)
            try:
                post.savers.remove(request.user)
                post.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def follow(request, username):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            user = User.objects.get(username=username)
            print(f".....................User: {user}......................")
            print(f".....................Follower: {request.user}......................")
            try:
                (follower, create) = Follower.objects.get_or_create(user=user)
                follower.followers.add(request.user)
                follower.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def unfollow(request, username):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            user = User.objects.get(username=username)
            print(f".....................User: {user}......................")
            print(f".....................Unfollower: {request.user}......................")
            try:
                follower = Follower.objects.get(user=user)
                follower.followers.remove(request.user)
                follower.save()
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))


@csrf_exempt
def comment(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            comment = data.get('comment_text')
            post = Post.objects.get(id=post_id)
            try:
                newcomment = Comment.objects.create(post=post,commenter=request.user,comment_content=comment)
                post.comment_count += 1
                post.save()
                print(newcomment.serialize())
                return JsonResponse([newcomment.serialize()], safe=False, status=201)
            except Exception as e:
                return HttpResponse(e)
    
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)
        comments = comments.order_by('-comment_time').all()
        return JsonResponse([comment.serialize() for comment in comments], safe=False)
    else:
        return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def delete_post(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            post = Post.objects.get(id=post_id)
            if request.user == post.creater:
                try:
                    delet = post.delete()
                    return HttpResponse(status=201)
                except Exception as e:
                    return HttpResponse(e)
            else:
                return HttpResponse(status=404)
        else:
            return HttpResponse("Method must be 'PUT'")
    else:
        return HttpResponseRedirect(reverse('login'))

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        
        # Update first and last name
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        
        # Update profile picture
        profile_pic = request.FILES.get('profile_pic')
        if profile_pic:
            user.profile_pic = profile_pic
        
        # Update cover image
        cover = request.FILES.get('cover')
        if cover:
            user.cover = cover
        
        # Update bio
        bio = request.POST.get('bio')
        if bio:
            user.bio = bio
        
        user.save()
        
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('profile', username=user.username)
    
    return render(request, 'network/edit_profile.html')
    
@login_required
def credits_view(request):
    user_credits, _ = UserCredits.objects.get_or_create(user=request.user)

    if request.method == "POST":
        code = request.POST.get("credit_code", "").strip()
        try:
            credit_code = CreditCode.objects.get(codigo=code)
            if credit_code.utilizado:
                messages.error(request, "Este código já foi utilizado.")
            else:
                credit_code.redeem(request.user)  
                messages.success(request, f"{credit_code.saldo} créditos adicionados!")
        except CreditCode.DoesNotExist:
            messages.error(request, "Código inválido.")

    return render(request, "network/credits.html", {
    "username": request.user.username,
    "saldo": user_credits.saldo
    })

def map_view(request):
    points = MapPoint.objects.all()
    points_data = [
        {
            "name": point.name,
            "description": point.description,
            "latitude": point.latitude,
            "longitude": point.longitude,
        }
        for point in points
    ]
    return render(request, 'map.html', {'points': json.dumps(points_data)})

def rewards(request):
    ofertas = Reward.objects.all()
    resgates_ids = Resgate.objects.filter(usuario=request.user).values_list('oferta_id', flat=True)
    user_credits = UserCredits.objects.filter(user=request.user).first()
    saldo = user_credits.saldo if user_credits else 0
    return render(request, 'network/rewards.html', {
        'ofertas': ofertas,
        'saldo': saldo,
        'resgates_ids': resgates_ids
    })

@login_required
def resgatar_oferta(request, oferta_id):
    if request.method == "POST":
        oferta = get_object_or_404(Reward, id=oferta_id)
        user_credits, _ = UserCredits.objects.get_or_create(user=request.user)

        if user_credits.saldo >= oferta.valor_em_creditos:
            # Descontar créditos
            user_credits.saldo -= oferta.valor_em_creditos
            user_credits.save()

            # Registrar o resgate
            Resgate.objects.create(usuario=request.user, oferta=oferta)

            messages.success(request, f"Oferta '{oferta.nome}' resgatada com sucesso!")
        else:
            messages.error(request, "Saldo insuficiente para resgatar esta oferta.")

        return HttpResponseRedirect(reverse("rewards"))

    return JsonResponse({"error": "Método inválido."}, status=400)





@login_required
def resgates(request):
    resgates = Resgate.objects.filter(usuario=request.user).select_related('oferta')
    return render(request, 'network/resgates.html', {'resgates': resgates})

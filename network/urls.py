
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path('n/mapa/', views.map_view, name='mapa'),
    path("loja/", include('ecommerce.loja.urls')),  
    path('pedido/', include('ecommerce.pedido.urls', namespace="pedido")), 
    path('perfil/', include('ecommerce.perfil.urls')),  
    path('produto/', include('ecommerce.produto.urls')), 
    path("n/login", views.login_view, name="login"),
    path("n/logout", views.logout_view, name="logout"),
    path("n/email", views.email, name="email"),
    path('enviar_email_pedido/', views.enviar_email_pedido, name='enviar_email_pedido'),
    path("n/register", views.register, name="register"),
    path("<str:username>", views.profile, name='profile'),
    path("n/following", views.following, name='following'),
    path("n/saved", views.saved, name="saved"),
    path('n/edit_profile/', views.edit_profile, name='edit_profile'),
    path("n/createpost", views.create_post, name="createpost"),
    path("n/post/<int:id>/like", views.like_post, name="likepost"),
    path("n/post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("n/post/<int:id>/save", views.save_post, name="savepost"),
    path("n/post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("n/post/<int:post_id>/comments", views.comment, name="comments"),
    path("n/post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path("n/post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("<str:username>/follow", views.follow, name="followuser"),
    path("<str:username>/unfollow", views.unfollow, name="unfollowuser"),
    path("n/post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path("n/resgatar_oferta", views.resgatar_oferta, name="resgatar_oferta"),
    path("n/rewards", views.rewards, name="rewards"),
    path("resgatar-oferta/<int:oferta_id>/", views.resgatar_oferta, name="resgatar_oferta"),
    path('resgates/', views.resgates, name='resgates'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


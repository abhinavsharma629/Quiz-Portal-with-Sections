from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static


urlpatterns = [
	# Quiz
    path('', LoginView.as_view(template_name='quizportal/login.html'), name="login"),
    path('detail/Section/<section_no>/<id_no>', views.detail, name='detail'),
    path('score/Section/<section_no>/<id_no>', views.score, name='score'),
    path('ended', views.ended, name='ended'),
    path('endSection/<section_no>', views.endSection, name='endSection'),
    # path('register', views.register, name='register'),
    path('admincsvupload/<section_no>', views.csvupload, name='csvupload'),
    path('admintimeupload/<section_no>', views.timeupload, name='timeupload'),
    path('adminmain', views.adminmain, name='adminmain'),
    path('DownloadUserData', views.DownloadUserData, name='DownloadUserData'),
    path('adminall', views.adminall, name='adminall'),
    path('regis', views.regis, name='regis'),
    path('admindelete/<nu>', views.admindelete, name='admindelete'),
    path('logout', LogoutView.as_view(template_name='quizportal/logout.html'), name="logout"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from home import views

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Lost And Found Item Portal"
admin.site.site_title = "Lost And Found Item Portal"
admin.site.index_title = "Lost And Found Item Portal"

urlpatterns = [
    path('', views.gettingStarted, name='gettingStarted'),
    path('register-page', views.registerpage, name='registerpage'),
    path('login-page', views.loginpage, name='login-page'),
    path('forgot-password', views.forgotPassword, name='forgot-password'),
    path('register-student', views.student_registration, name='register-student'),
    path('login-student', views.studentLogin, name='login-student'),
    path('add-item-page', views.addItempage, name='add-item-page'),
    path('add-item', views.add_item, name='add_item'),
    path('item-list', views.item_list, name='item_list'),
    path('claim-item/<int:item_id>/', views.claim_item, name='claim_item'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

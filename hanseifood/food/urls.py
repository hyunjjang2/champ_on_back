from django.urls import path
from django.contrib import admin
from .views import base_views, menu_views, ticket_views, login_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


urlpatterns = [
    # /views/base_views
    path("", base_views.index, name="index"),
    path('admin/', admin.site.urls),

    # /views/menu_views
    path('menus/day', menu_views.get_todays_menu, name='daily_menu'),
    path('menus/week', menu_views.get_weekly_menus, name='weekly_menu'),
    path('menus/target', menu_views.get_target_days_menu, name='target_menu'),
    path("login", login_views.try_login, name = 'try_login'),
    # path("verifyuser", login_views.verify_user, name = 'code'),
    # path("logout", login_views.logout, name = 'logout'),
    path("nickname", login_views.set_nickname, name ="set_nickname"),
    path('api/token', login_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # /views/ticket_views
    path('tickets/validate/<str:ticket_id>', ticket_views.get_ticket_validation, name='validate_ticket')
]

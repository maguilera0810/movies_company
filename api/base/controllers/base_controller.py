from api.base.permissions.base_permisions import (AdminPermission,
                                                  AuthPermission,
                                                  BasicPermission, OnlyAuthPermission)
from django.conf import settings
from rest_framework import viewsets

DEBUG = settings.DEBUG


class BaseController(viewsets.ViewSet):
    """

    Base Controller:

    It will works with all users

    """
    permission_classes = [BasicPermission, ]


class IsAuthController(viewsets.ViewSet):
    """
    IsAuthController:

    It will works only when the user is authenticated

    """

    permission_classes = [AuthPermission, ]

class IsOnlyAuthController(viewsets.ViewSet):
    """
    IsAuthController:

    It will works only when the user is authenticated

    """

    permission_classes = [OnlyAuthPermission, ]



class IsAdminController(viewsets.ViewSet):
    """
    IsAuthController:

    It will works only when the user is an authenticated admin

    """
    permission_classes = [AdminPermission, ]

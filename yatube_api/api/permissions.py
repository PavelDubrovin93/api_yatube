from rest_framework import permissions


class OwnerOrAuthReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
    '''
    request.method in permissions.SAFE_METHODS.

    test_post_not_auth и test_comment_get_unauth,
    ломаются с этим услословием.

    "AssertionError: Проверьте, что при GET-запросе
    неавторизованного пользователя к
    `/api/v1/posts/`|`/api/v1/posts/{post.id}/comments/`
    возвращается ответ со статусом 401."
    '''

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

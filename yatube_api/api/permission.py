from rest_framework.permissions import BasePermission, SAFE_METHODS
# его и использую, не хочет хоткеем в этом месте, странно


class IsAuthorOrReadOnly(BasePermission):
    """Проверяет, является ли пользователь автором поста."""

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
        )

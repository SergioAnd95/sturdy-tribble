from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AdminRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = ('is_staff', 'is_active')

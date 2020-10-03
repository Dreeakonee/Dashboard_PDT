from django.shortcuts import redirect

class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('erp:dashboard') #### NO SE QUE PONER *********************
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        if 'group' in request.session:
            group = request.session['group']
            #group = Group.objects.get(pk=1)
            if group.permissions.filter(codename=self.permission_required):
                return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())


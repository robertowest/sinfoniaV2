from django.shortcuts import render


class AuditableMixin(object,):
    """Se utilizará para grabar la información del usuario actual"""
    def form_valid(self, form, ):
        if not form.instance.created_by:
            form.instance.created_by = self.request.user
        form.instance.modified_by = self.request.user
        return super(AuditableMixin, self).form_valid(form)

import os
import threading

from django.http import HttpResponseRedirect

from django_tables2 import SingleTableView

def get_template_path(appname, template):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = "{path}/{app}/templates/{app}/{html}".format(path=path, app=appname, html=template)
    if os.path.exists(file):
        template_name = "{app}/{html}".format(app=appname, html=template)
    else:
        template_name = "comunes/{html}".format(html=template)
    return template_name


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = "filter"

    def get_table_data(self):
        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data()
        )
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data(**kwargs)
        context[self.context_filter_name] = self.filter
        return context


_thread_locals = threading.local()

def set_current_user(user):
    _thread_locals.user = user


def get_current_user():
    return getattr(_thread_locals, 'user', None)


def where_are_we_going(self, response):
    # terminamos, ¿hacia dónde vamos?
    if self.request.GET.get('next'):
        return HttpResponseRedirect(self.request.GET.get('next'))
    elif 'previous_url' in self.request._post:
        return HttpResponseRedirect(self.request._post['previous_url'])
    elif self.success_url:
        return HttpResponseRedirect(self.success_url)
    else:
        return response
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MailboxAngular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^messages/send/', 'ngmail.views.send_message'),
    url(r'^messages/([0-9a-zA-Z]+)/move/', 'ngmail.views.move_messages'),
    url(r'^messages/([0-9a-zA-Z]+)/', 'ngmail.views.messages'),
    url(r'^message/([0-9]+)/', 'ngmail.views.get_message'),
    url(r'^user/add/','ngmail.views.add_user'),
    url(r'^user/([0-9]+)/edit/', 'ngmail.views.edit_user'),
    url(r'^user/([0-9]+)/delete/', 'ngmail.views.delete_contact'),
    url(r'^user/([0-9]+)/activate/', 'ngmail.views.activate_contact'),
    url(r'^user/([0-9]+)/', 'ngmail.views.user'),
    url(r'^folders/', 'ngmail.views.folders'),
    url(r'^folder/create/([0-9a-zA-Z]+)/', 'ngmail.views.create_folder'),
    url(r'^folder/delete/([0-9a-zA-Z]+)/', 'ngmail.views.delete_folder'),
    url(r'^users/deleted/', 'ngmail.views.deleted_users'),
    url(r'^users/', 'ngmail.views.users'),
    url(r'^admin/', include(admin.site.urls)),
)

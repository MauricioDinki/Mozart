# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

from Profiles.views import ProfileSettingsView, ChangePasswordView, SocialNetworkSettingsView, ProfileView, PromoterListView

urlpatterns = patterns(
    '',
    url(r'^promoters/$', PromoterListView.as_view(), name='promoters_list'),
    url(r'^profiles/(?P<username>.*)/$', ProfileView.as_view(), name='user_profile'),
    url(r'^settings/account/', ProfileSettingsView.as_view(), name='settings_account'),
    url(r'^settings/password/', ChangePasswordView.as_view(), name='settings_password'),
    url(r'^settings/social/$', SocialNetworkSettingsView.as_view(), name='settings_social'),
    url(r'^settings/social/(?P<provider>.*)/(?P<account_id>.*)/delete$', 'Profiles.views.SocialNetworkDeleteView', name='settings_social_delete'),
)

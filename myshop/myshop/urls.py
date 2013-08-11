from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# overiding the promotion app:
# 1  The oscar Shop Class has apps. one of them is promotions_app.
# 2. subclass a promotions class:
#    from oscar.apps.promotions.app import PromotionsApplication
#    class MyPromotionsApplication( PromotionsApplication ): ...
#    myPromotionsApp = MyPromotionsApplication()
# 3. subclass the Shop, and override the promotions_app:
#    from oscar.app import Shop
#    class BaseApplication( Shop ):
#       promotions_app = myPromotionsApp
# 4. setting file: INSTALLED_APP + get_core_apps(['myshop.apps.promotions'])
from myshop.app import application


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'', include(application.urls)),
    # Examples:
    # url(r'^$', 'myshop.views.home', name='home'),
    # url(r'^myshop/', include('myshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)

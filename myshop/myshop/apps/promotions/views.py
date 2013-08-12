from oscar.apps.promotions.views import HomeView

class MyHomeView(HomeView):
    template_name = 'new-homeview.html'

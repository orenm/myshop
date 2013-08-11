from oscar.apps.promotions.views import HomeView as CoreHomeView

class HomeView(CoreHomeView):
    import pdb;pdb.set_trace()
    template_name = 'promotions/new-homeview.html'

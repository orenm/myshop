from oscar.apps.promotions.app import PromotionsApplication
from myshop.apps.promotions.views import MyHomeView

class MyPromotionsApplication( PromotionsApplication ):
    home_view = MyHomeView

myPromotionsApp = MyPromotionsApplication()

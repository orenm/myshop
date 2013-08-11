from myshop.apps.promotions.app import myPromotionsApp

# override the original oscar shop with my own.
# override the promotions_app in the new class.
from oscar.app import Shop
class BaseApplication( Shop ):
    promotions_app = myPromotionsApp

application = BaseApplication()

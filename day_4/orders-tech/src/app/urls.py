from django.urls import path
#from django.db import router

# rest_framework
from rest_framework.routers import DefaultRouter

# views
#from .viewsets.views import OrderViewSet,ComponentsViewSet,KeyboardViewSet, MouseViewSet, DisplayViewSet, SpeakerViewSet, MotherBoardViewSet, ProcessorViewSet, ComputerViewSet, ComponentsListView

from .viewsets.component import KeyboardViewSet, MouseViewSet, DisplayViewSet, SpeakerViewSet, MotherBoardViewSet, ProcessorViewSet
from .viewsets.computer import ComputerViewSet
from .viewsets.order import OrderViewSet, OrderDetailComputerViewSet

router = DefaultRouter()
router.register(r'keyboard', KeyboardViewSet)
router.register(r'mouse', MouseViewSet)
router.register(r'display', DisplayViewSet)
router.register(r'speaker', SpeakerViewSet)
router.register(r'motherboard', MotherBoardViewSet)
router.register(r'processor', ProcessorViewSet)
router.register(r'computer', ComputerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderdetailcomputer', OrderDetailComputerViewSet)
#router.register(r'components', ComponentsViewSet)
#router.register(r'orders', OrderViewSet)

urlpatterns = router.urls

urlpatterns += [
   #path('components/', ComponentsListView.as_view(), name='ComponentsListView'),

]
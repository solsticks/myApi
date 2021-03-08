from webapi.viewsets import employeesViewset
from webapi.viewsets import ProductViewset
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('employees', employeesViewset)
routers.register('products', ProductViewset)


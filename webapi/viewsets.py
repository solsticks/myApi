from rest_framework import viewsets
from . import models
from . import serialize


class employeesViewset(viewsets.ModelViewSet):
    queryset = models.employees.objects.all()
    serializer_class = serialize.employeesSerializers


class ProductViewset(viewsets.ModelViewSet):
    queryset = models.product.objects.all()
    serializer_class = serialize.ProductSerializers

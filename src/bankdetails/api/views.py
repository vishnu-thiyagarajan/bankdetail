# Create your views here.
from rest_framework import generics
from bankdetails.models import BankDetails
from .serializers import ActionSerializer
from rest_framework.permissions import IsAuthenticated


class GetBankDetails(generics.RetrieveAPIView):
    lookup_feild = 'ifsc'
    permission_classes = (IsAuthenticated,)
    serializer_class = ActionSerializer

    def get_object(self):
        ifsc = self.kwargs.get("ifsc")
        val = BankDetails.objects.get(ifsc=ifsc)
        return val


class GetListBankDetails(generics.ListAPIView):
    lookup_feild = ('bank_name', 'city')
    permission_classes = (IsAuthenticated,)
    serializer_class = ActionSerializer

    def get_queryset(self):
        bank_name = self.kwargs.get("bank_name")
        city = self.kwargs.get("city")
        return BankDetails.objects.filter(bank_name=bank_name, city=city)

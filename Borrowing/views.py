from rest_framework import viewsets

from Borrowing.models import Borrowing
from Borrowing.serializers import BorrowingListSerializer, BorrowingDitailSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        return BorrowingDitailSerializer

    def perform_create(self, serializer):
        serializer.save(User_id=self.request.user)

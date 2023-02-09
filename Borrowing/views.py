from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets

import Customer.models
from Borrowing.models import Borrowing
from Borrowing.serializers import BorrowingListSerializer, BorrowingDitailSerializer, BorrowingCreateSerializer, \
    BorrowingUpdateSerializer
from Borrowing.permissions import OnlyForAuthenticatedUser
from book.models import Book
from messager import send_to_telegram


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    permission_classes = (OnlyForAuthenticatedUser,)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "create":
            return BorrowingCreateSerializer
        if self.action == "update":
            return BorrowingUpdateSerializer
        return BorrowingDitailSerializer

    def perform_create(self, serializer):
        serializer.save(User_id=self.request.user)
        book_id = serializer.data["Book_id"]
        book = Book.objects.get(id=book_id)
        try:
            send_to_telegram(
                message=f"Hi, you borrowed {book.Title}, "
                        "on site Library.com, nice reading",
                user=self.request.user
            )
        except Customer.models.TelegramChat.DoesNotExist:
            pass

    def get_queryset(self):
        if self.request.user.is_staff is False:
            return self.queryset.filter(User_id=self.request.user)
        user_id = self.request.query_params.get("user_id")
        if self.request.user.is_staff and user_id:
            return self.queryset.filter(User_id=user_id)
        is_active = self.request.query_params.get("is_active")
        if is_active:
            return self.queryset.filter(Actual_return_date=None)
        return self.queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "is_active",
                type={"type": "list", "items": {"type": "string"}},
                description="Filter by those who returned books"
                            "(ex. ?is_active=None)",
            ),
            OpenApiParameter(
                "user_id",
                type={"type": "list", "items": {"type": "integer"}},
                description="user debt filter"
                            "(ex. ?user_id=1)",
            ),
            ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


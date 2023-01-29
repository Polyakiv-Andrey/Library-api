from rest_framework import serializers

from Borrowing.models import Borrowing
from book.serializers import BookSerializer


class BorrowingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = "__all__"


class BorrowingDitailSerializer(BorrowingListSerializer):
    Book_id = BookSerializer(many=True, read_only=True)


class BorrowingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = ("id", "Book_id", "Expected_return_date")

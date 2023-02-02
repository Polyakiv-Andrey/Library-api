import datetime

from rest_framework import serializers

from Borrowing.models import Borrowing
from book.serializers import BookSerializer


class BorrowingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = "__all__"


class BorrowingDitailSerializer(BorrowingListSerializer):
    Book_id = BookSerializer(many=False, read_only=True)


class BorrowingCreateSerializer(BorrowingListSerializer):

    class Meta:
        model = Borrowing
        fields = ("id", "Book_id", "Expected_return_date")

    def create(self, validated_data):
        if validated_data["Book_id"].Inventory == 0:
            raise ValueError("Unfortunately we have not that book now")
        book = validated_data["Book_id"]
        book.Inventory -= 1
        book.save()
        return Borrowing.objects.create(**validated_data)


class BorrowingUpdateSerializer(BorrowingListSerializer):
    Expected_return_date = serializers.DateTimeField(read_only=True)
    Actual_return_date = serializers.DateTimeField(read_only=True)
    Book_id = BookSerializer(read_only=True)
    User_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Borrowing
        fields = "__all__"

    def update(self, instance, validated_data):
        if instance.Actual_return_date is None:
            instance.Actual_return_date = datetime.datetime.now()
            book = instance.Book_id
            book.Inventory += 1
            book.save()
            instance.save()
        return instance

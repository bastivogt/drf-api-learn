from rest_framework import serializers

from .models import Author, Book




class AuthorInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title"
        ]


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorInlineSerializer(many=True)
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        autors_data = validated_data.pop("authors")
        book = Book.objects.create(**validated_data)
        print(autors_data)
        for author_data in autors_data:
            print(author_data)
            a = Author.objects.create(first_name=author_data["first_name"], last_name=author_data["last_name"])
            book.authors.add(a)
        return book
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        authors_data = validated_data.pop("authors")
        count = 0
        for a in instance.authors.all():
            a.first_name = authors_data[count]["first_name"]
            a.last_name = authors_data[count]["last_name"]
            a.save()
            count += 1
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    books = BookInlineSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = "__all__"



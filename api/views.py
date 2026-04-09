from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Telefon
from .serializers import TelefonSeralizer


class MyApi(APIView):

    def get(self, request):
        telefons = Telefon.objects.all()
        serializer = TelefonSeralizer(telefons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request.data ni serializatorga uzatish kerak
        serializer = TelefonSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 'name' maydoni saqlangan ma'lumotdan olinadi
            name = serializer.validated_data.get("name")
            return Response(
                {"message": f"{name} telefon qo'shildi."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        new_name = request.data.get("new_name")
        obj_id = request.data.get(
            "id"
        )  # 'id' built-in funksiya nomi, o'zgaruvchi uchun 'obj_id' yaxshiroq

        try:
            telefon = Telefon.objects.get(id=obj_id)
            telefon.name = new_name
            telefon.save()
            return Response({"message": "Saqlandi chotkiy"}, status=status.HTTP_200_OK) # noqa
        except Telefon.DoesNotExist:
            return Response(
                {"error": "Kechirasiz, telefon topilmadi."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def __str___(self):
        return self.name

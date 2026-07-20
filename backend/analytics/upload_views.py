import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Site, EnergyReading

class UploadCSVView(APIView):

    def post(self, request):

        if 'file' not in request.FILES:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        csv_file = request.FILES['file']

        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():

            site = Site.objects.get(id=row["site"])

            EnergyReading.objects.create(
                site=site,
                timestamp=row["timestamp"],
                imported_kwh=row["imported_kwh"],
                exported_kwh=row["exported_kwh"],
                solar_generation_kwh=row["solar_generation_kwh"]
            )

        return Response(
            {"message": "CSV uploaded successfully"},
            status=status.HTTP_201_CREATED
        )
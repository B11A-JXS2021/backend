from .models import Drive
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from datetime import datetime, date, timedelta
from .serializers import DriveSerializer


def weekRange(year, week):
    start_of_year = date(year, 1, 1)
    now = start_of_year + timedelta(weeks=week+1)
    sun = now - timedelta(days=now.isoweekday() % 7)
    week_li = []
    week_li.append(sun)
    week_li.append(sun + timedelta(days=6))
    return week_li

class DriveData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        accel_x = request.data.get("accel_x")
        accel_y = request.data.get("accel_y")
        accel_z = request.data.get("accel_z")
        drive_obj = Drive(user=user, accel_x=accel_x, accel_y=accel_y, accel_z=accel_z, timestamp=datetime.now())
        serializer = DriveSerializer(drive_obj)
        if serializer.is_valid:
            drive_obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        week_num = int(request.data.get("week_num"))
        drive_obj = Drive.objects.filter(user=user)
        dt = datetime.now()
        year = dt.year
        week = dt.isocalendar()[1] - week_num
        week_range = weekRange(year, week)
        week_start = week_range[0]
        week_end = week_range[1]
        filtered_drive = drive_obj.filter(timestamp__range=[week_start, week_end])
        serializer = DriveSerializer(filtered_drive, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

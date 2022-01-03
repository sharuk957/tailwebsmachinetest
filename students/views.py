from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Student, Subject
from .serializer import StudentSerializer, SubjectSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class SubjectView(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        subject = request.data.get('subject')
        user = request.user
        subject_instance = Subject.objects.filter(subject=subject,user=user).first()
        if subject_instance:
            return Response({"message":"Subject already Exists"},status=status.HTTP_208_ALREADY_REPORTED)
        update_request = request.data.copy()
        update_request.update({'user':user.id})
        print(update_request)
        serializer = self.get_serializer(data=update_request)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message":"successfully created"},status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = Subject.objects.filter(user=request.user)
        serializer = SubjectSerializer(queryset,many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        subject = request.data.get('subject')
        user = request.user
        instance = self.get_object()
        if instance.subject != subject:
            subject_instance= Subject.objects.filter(user=user,subject=subject).first()
            if subject_instance:
                return Response({"message":"Subject already Exists"},status=status.HTTP_208_ALREADY_REPORTED)
        partial = True
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        name = request.data.get('name')
        subject = Subject.objects.filter(subject=request.data.get('subject'),user=user).first()
        mark = request.data.get('mark')
        subject_instance = Student.objects.filter(name=name,subject=subject,user=user).first()
        if subject_instance:
            subject_instance.mark = subject_instance.mark + int(mark)
            subject_instance.save()
        else:
            Student.objects.create(name=name,user=user,subject=subject,mark=mark)
        return Response({"message":"successfully registered"},status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        data = Student.objects.filter(user=request.user)
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        name = request.data.get('name')
        subject = Subject.objects.filter(id=request.data.get('subject')).first()
        if instance.subject != subject or instance.name != name:
            subject_instance = Student.objects.filter(name=name,subject=subject.id,user=user).first()
            print(subject_instance)
            if subject_instance:
                return Response({"message":"the same field is  already Exists"},status=status.HTTP_208_ALREADY_REPORTED)
        partial = True
        update_request = request.data.copy()
        update_request.update({'subject':subject.id,'user':user.id})
        serializer = self.get_serializer(instance, data=update_request, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
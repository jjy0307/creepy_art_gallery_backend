from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from django.contrib.auth import login, logout, authenticate

from user.serializers import UserSignupSerializer, UserSignupSerializer

from user.jwt_claim_serializer import JwtTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(APIView):
    def get(self, request):
        return Response(UserSignupSerializer(request.user).data, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입 완료!!"})
        else:
            print(serializer.errors)
            return Response({"message": "가입 실패!!"})


class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        user_id = request.data.get('user_id', '')
        password = request.data.get('password', '')

        user = authenticate(request, user_id=user_id, password=password)

        if not user:
            return Response({"error": "존재하지 않는 아이디이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})


class JwtTokenObtainPairView(TokenObtainPairView):
    serializer_class = JwtTokenObtainPairSerializer

    # 인가된 사용자만 접근할 수 있는 View 생성


class OnlyAuthenticatedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # JWT 인증방식 클래스 지정하기
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        # Token에서 인증된 user만 가져온다.
        user = request.user
        if not user:
            return Response({"error": "접근 권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "인증 성공!"})

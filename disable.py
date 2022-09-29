# from urllib import request
#
# from fastapi import APIRouter, HTTPException, Depends
# from fastapi.openapi.models import Response
# from jwt import jwt
# from starlette.authentication import BaseUser
#
# import db
#
# disable_router = APIRouter()
#
#
# @disable_router.post("/status/")
# def status(email: str, password: str):
#     email = request.data.get("email")
#     token = request.headers.get("Authorization")
#     token = jwt.decode(token, "secret", algorithms=["HS256"])
#     user = db.session.query(db.User).filter(db.User.email_id == email).first()  # BaseUser.objects.get(id=token['id'])
#
#     # print(user.is_opsuser)
#     client = BaseUser.objects.all()
#     if user.is_opsuser:
#         cl_user = BaseUser.objects.get(email=email)
#         if cl_user:
#             if cl_user.is_opsuser:
#                 return Response({"message": "Sorry , its an Ops user"})
#             elif cl_user.is_active:
#
#                 cl_user.is_active = False
#                 cl_user.save()
#                 return Response({"message": "client with email" + email + " is disabled"})
#             else:
#                 cl_user.is_active = True
#                 cl_user.save()
#                 return Response({"message": "client with email" + email + " is enabled"})
#
#         else:
#             return Response({"message": "Email doesnt exist"})
#     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from backend.repository.user import UserRepository
from backend.repository.session import SessionRepository
from fastapi import APIRouter, Depends, Header

router = APIRouter(prefix="/user")

@router.get("/")
async def get_user(user_id: str,
authorization: str = Header(None),
user_repository: UserRepository = Depends(),
session_repository: SessionRepository = Depends()
):
    if(session_repository.validate(authorization[7:], user_id)):
        return user_repository.find_by_id(user_id)
    return dict(error="Invalid token.")

# @router.get("/")
# async def get(
# request: Request
# ) -> None:
#   # print(user_id)
# #   print(getattr(request, 'headers'))
#   print(request.__dict__)
#     # if(session_repository.validate(access_token=access_token, 
#     #   user_id=user_id) == False):
#     #   return dict(error="Invalid token provided.")
#     # return settings_repository.get(user_id)
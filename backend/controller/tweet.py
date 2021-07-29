import tweepy
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Credentials(BaseModel):
    accessToken: str
    idToken: str

@router.post("/tweet")
async def tweet(tweet: str, credentials: Credentials) -> str:
        auth = tweepy.OAuthHandler(
            "JRt64Cxv5rGV9vkPApbbakLQd",
            "LtJmNaoPATfMZrJ6JHrqy5qWPKi4YTpRD9gFjyTWzs9UfdDCTr",
        )
        auth.set_access_token(credentials.accessToken, credentials.idToken)
        twitter = tweepy.API(auth)
        twitter.update_status(status=tweet)
        return tweet

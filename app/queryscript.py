from fastapi import APIRouter

router = APIRouter()

@router.get("/field/[id]")
def start_query():
    # function needs to be able to query through database of industry questions and return a valid set of questions
    pass



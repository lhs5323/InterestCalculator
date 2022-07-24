import json
from fastapi import APIRouter

router = APIRouter()

@router.get('/result')
async def main():
    return {'hi'}
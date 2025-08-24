from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database.database import get_db
from app.database.models import Log
from ..services.openai_service import generate_natal_card


router = APIRouter(prefix="/astro", tags=["astro"])


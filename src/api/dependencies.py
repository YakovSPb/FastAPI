from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_sesstion


SessionDep = Annotated[AsyncSession, Depends(get_sesstion)]

from sqlalchemy import String,ForeignKey
from datetime import datetime
from typing import Optional,List
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import mapped_column, Mapped, relationship

from config.settings import Base
from apps.users.models import Users

class Payments(Base):
    STATUSES=(
        ('IN-PROCESS','in-process'),('SUCCESS','success'),('DENIED', 'denied')
    )
    __tablename__='payments'
    id: Mapped[int]=mapped_column(primary_key=True)
    amount:Mapped[float]
    status=mapped_column(ChoiceType(choices=STATUSES))
    datetime:Mapped[datetime]
    
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    user:Mapped['Users']=relationship(Users,lazy="joined")


     

    def __str__(self) -> str:
        return self.name
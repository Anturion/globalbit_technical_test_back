from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class StatePaymentEnum(str, Enum):

    rechazada = u'rechazada',
    en_proceso = u'en-proceso',
    aprobada = u'aprobada'


class PaymentCreate(BaseModel):

    email: str
    amount: float
    state: StatePaymentEnum
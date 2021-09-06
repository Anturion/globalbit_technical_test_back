import random
import string
from datetime import datetime
from sqlalchemy.orm import Session
from sql_app import models, security, schemas, crud

def create_payment(db: Session, payment: schemas.payments.PaymentCreate):
    print(payment.email)

    user = crud.users.get_user_by_email(db, payment.email)

    if not user:
        return False

    db_payment = models.Payments(
        id=random.randint(10000000,99999999),
        id_client=user.id,
        amount=payment.amount,
        date=datetime.now(),
        state=payment.state
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

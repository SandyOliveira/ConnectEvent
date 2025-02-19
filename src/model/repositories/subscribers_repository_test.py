import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info={
        "name":"Anna",
        "email":"a@email.com",
        "evento_id":3
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)
    
@pytest.mark.skip("select in DB")
 
def test_select_subscriber():
    email = "a@email.com"
    evento_id = 3
    
    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email,evento_id)
    print(resp.nome)
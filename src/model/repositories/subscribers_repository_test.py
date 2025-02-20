import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info={
        "name":"João",
        "email":"j@email.com",
        "evento_id":4
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

@pytest.mark.skip("select rankingin DB")
def test_ranking():
    evento_id = 3
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)
    print()

    for elem in resp:
        print(f"Link: {elem.link}, total de inscritos: {elem.total}")
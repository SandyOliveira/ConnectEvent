from flask import Blueprint,jsonify, request

subs_route_bp =Blueprint("subs_route",__name__)

from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.model.repositories.subscribers_repository import SubscribersRepository

from src.controllers.subscribers.subscribers_creator import SubscribersCreator


@subs_route_bp.route("/subscriber",methods=["POST"])

def create_new_subs():
    #validação
    subscribers_creator_validator(request)
    #separação do que precisa para a requisição
    http_request = HttpRequest(body=request.json)
    
    #criando a logica com o db
    subs_repo = SubscribersRepository()
    subs_creator = SubscribersCreator(subs_repo)
    
    http_response = subs_creator.create(http_request)
    
    #http_response = HttpResponse(body={"local":"aqui"},status_code =201)
    return jsonify(http_response.body),http_response.status_code
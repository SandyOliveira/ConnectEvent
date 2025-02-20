from flask import Blueprint,jsonify, request

event_route_bp =Blueprint("event_route",__name__)

from src.validators.events_creator_validator import events_creator_validator



from src.http_types.http_request import HttpRequest


from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route("/event",methods=["POST"])

def create_new_event():
    #validação
    events_creator_validator(request)
    #separação do que precisa para a requisição
    http_request = HttpRequest(body=request.json)
    
    #criando a logica com o db
    eventos_repo = EventosRepository()
    events_creator = EventsCreator(eventos_repo)
    
    http_response = events_creator.create(http_request)
    
    #http_response = HttpResponse(body={"local":"aqui"},status_code =201)
    return jsonify(http_response.body),http_response.status_code


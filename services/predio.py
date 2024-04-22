from flask import Blueprint, request, jsonify
from model.predio import Predio
from model.tipo_predio import TipoPredio
from utils.db import db

predios=Blueprint('predios',__name__)

@predios.route('/predios/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='241-flask-crud-backend-master'
    return jsonify(result)

@predios.route('/predios/v1/listar',methods=['GET'])
def getPredios():
    result={}
    predios=Predio.query.all()    
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se recupero los predios sin inconvenientes"
    return jsonify(result),200

@predios.route('/predios/v1/insert',methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    predio=Predio(id_tipo_predio,descripcion,ruc,telefono,correo,direccion,idubigeo)
    db.session.add(predio)
    db.session.commit()
    result["data"]=predio
    result["status_code"]=201
    result["msg"]="Se agrego el predio"
    return jsonify(result),201

@predios.route('/predios/v1/update',methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    predio=Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="predio no existe"
        return jsonify(result),400
    
    predio.id_tipo_predio=id_tipo_predio
    predio.descripcion=descripcion
    predio.ruc=ruc    
    predio.telefono=telefono
    predio.correo=correo
    predio.direccion=direccion
    predio.idubigeo=idubigeo

    db.session.commit()
    
    result["data"]=predio
    result["status_code"]=202
    result["msg"]="Se modificó el predio"
    return jsonify(result),202

@predios.route('/predios/v1/delete',methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')   
    #verificacion del id 
    if not id_predio:
        result["status_code"]=400
        result["msg"]="Debe consignar un id de previo valido"
        return jsonify(result),400
    # se encontro el predio
    predio=Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="Predio no existe"
        return jsonify(result),400
    
    db.session.delete(predio)
    db.session.commit()
    
    result["data"]=predio
    result["status_code"]=200
    result["msg"]="Se eliminó el predio"
    return jsonify(result),200
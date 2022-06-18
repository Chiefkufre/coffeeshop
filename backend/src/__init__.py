from flask import Flask, request, redirect, abort, jsonify
from flask_cors import CORS
from .models import setup_db, db_drop_and_create_all, Drink
from sqlalchemy import exc
import json
import os
# from .auth import AuthError, requires_aut


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Method', 'GET, POST, DELETE, PATCH, PUT')
        return response
    
    
    '''
    @TODO uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
    db_drop_and_create_all()

    # ROUTES
    '''
    @TODO implement endpoint
        GET /drinks
            it should be a public endpoint
            it should contain only the drink.short() data representation
        returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
            or appropriate status code indicating reason for failure
    '''

    @app.route('/drinks')
    def get_drink():
        page = request.args.get('page', 1,type=int)
        per_page = request.args.get('per_page', 1,type=int)
        
        try:
            drinks = Drink.query.order_by(Drink.id).paginate(page=page, per_page=per_page)
            
            if drinks is None:
                return jsonify({
                    "msg": 'Drinks not found'
                }),404
            
            else:
                # data = []
                for drink in drinks.items:
                    moredrinks = drink.short()
                    # data.append({
                    #     "drinkId": drink.id,
                    #     "drinkTitle": drink.title,
                    #     "Recipe": drink.recipe         
                    # })
                
            return jsonify({
                "success": True,
                "drinks": moredrinks
            }), 200
        
        except:
            abort(404)
            
    
    # get drink by id
    @app.route('/drinks/<int:id>')
    def get_drink_by_id(id):
        page = request.args.get('page', 1,type=int)
        per_page = request.args.get('per_page', 1,type=int)
        
        try:
            drinks = Drink.query.filter(Drink.id==id).paginate(page=page, per_page=per_page)
            
            if drinks is None:
                return jsonify({
                    "msg": 'Drinks not found'
                }),404
            
            else:
                data = []
                for drink in drinks.items:
                    data.append({
                        "drinkId": drink.id,
                        "drinkTitle": drink.title,
                        "Recipe": drink.recipe         
                    })
                
            return jsonify({
                "success": True,
                "drinks": data
            }), 200
        
        except:
            abort(404)



    '''
    @TODO implement endpoint
        GET /drinks-detail
            it should require the 'get:drinks-detail' permission
            it should contain the drink.long() data representation
        returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
            or appropriate status code indicating reason for failure
    '''
    @app.get('/drink-detail')
    def drinks_details():
        page = request.args.get('page', 1,type=int)
        per_page = request.args.get('per_page', 1,type=int)
        
        try:
            drinks = Drink.query.order_by(Drink.id).paginate(page=page, per_page=per_page)
            
            if drinks is None:
                return jsonify({
                    "msg": 'Drinks not found'
                }),404
            
            else:
                # data = []
                for drink in drinks.items:
                    moredrinks = drink.long()
                    # data.append({
                    #     "drinkId": drink.id,
                    #     "drinkTitle": drink.title,
                    #     "Recipe": drink.recipe         
                    # })
                
            return jsonify({
                "success": True,
                "drinks": moredrinks
            }), 200
        
        except:
            abort(404)


    '''
    @TODO implement endpoint
        POST /drinks
            it should create a new row in the drinks table
            it should require the 'post:drinks' permission
            it should contain the drink.long() data representation
        returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
            or appropriate status code indicating reason for failure
    '''
    @app.post('/drinks')
    def add_drinks():
        
        new_title = request.json.get('title', None)
        new_recipe = request.json.get('recipe', None)
        
        try:
            if Drink.query.filter_by(title=new_title).first() is not None:
                return jsonify({
                    "msg": f'{Drink.tile} is availabel'
                }), 409
            
            else:
                new_drink = Drink(title=new_title, recipe=new_recipe)
                new_drink.insert()
                
            return jsonify({
                'success': True,
                'msg': 'drink created',
                'new_drink':{
                    'title': new_drink.title
                },
                'drinks':[new_drink.long()]   
            }),201
        except:
            abort(400)



    '''
    @TODO implement endpoint
        PATCH /drinks/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should update the corresponding row for <id>
            it should require the 'patch:drinks' permission
            it should contain the drink.long() data representation
        returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
            or appropriate status code indicating reason for failure
    '''
    @app.patch('/drinks/<int:id>')
    def update_drinks(id):
        drinks = Drink.query.filter(Drink.id==id).one_or_none()
        
        if not drink:
            abort(404)

        else:
            try:
                bud = request.get_json()
                req_title = bud.get('title')
                req_recipe = bud.get('recipe')
                
                if req_title:
                    drink.title = req_title
                    
                if req_recipe:
                    drink.recipe = json.dumps(bud['recipe'])

                drink.update()
            except:
                abort(400)
                
        return jsonify({
            "success": True,
            "drinks": drinks
        }),200

    '''
    @TODO implement endpoint
        DELETE /drinks/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should delete the corresponding row for <id>
            it should require the 'delete:drinks' permission
        returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
            or appropriate status code indicating reason for failure
    '''
    @app.delete('/drinks/<int:id>')
    def delete_drinks(id):
        drinks = Drink.query.filter(Drink.id==id).one_or_none()
        
        try:
            if drinks is None:
                return jsonify({
                    "msg": "Drink not found"
                }), 404
            else:
                drinks.delete()     
            
            return jsonify({
                "success": True,
                "delete": drinks.id
            }),201
        
        except:
            abort(404)


    # Error Handling
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Not Processable"
        }), 422


    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500



    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above
    '''
    
    return app
    
    
from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

recipes = {
    1:{
        'id' : 1,
        'bread' : '2 slices',
        'turkey' : '4 slices',
        'swiss cheese' : '1 slice',
        'mayonnaise' : '1 teaspoon',
        'recipe' : 'turkey sandwich'
    },
    2:{
        'id' : 2,
        'bread' : '2 slices',
        'peanut butter' : '1 teaspoon',
        'strawberry jam' : '1 teaspoon',
        'recipe' : 'pb & j'
    }
}

posts = {
    1 : {
        'author' : 2,
        'title' : 'my pb & j',
        'body' : 'sandwich I make for a quick snack'
    },
    2 : {
        'author' : 1,
        'title' : 'turkey sandwich for lunch',
        'body' : 'sandwich I always take to work'
    }
}

@app.route('/')
def land():
    return {
        "you've officially landed the REAL PAGE!" : "Welcome young Padawans to Flask!"
    }

@app.route('/recipes')
def get_recipes():
    return {
        'recipes' : list(recipes.values())
    }

@app.route('/recipe/<int:id>')
def get_ind_recipes(id):
    if id in recipes:
        return{
            'recipe' : recipes[id]
        }
    return{
        'UH OH, something went wrong' :"Invalid recipe id"
    }

@app.route('/recipes', methods=["POST"])
def create_recipe():
    data = request.get_json()
    print(data)
    recipes[data['id']] = data
    return {
        'recipe created successfully': recipes[data['id']]
    }

@app.route('/recipes', methods=["PUT"])
def update_recipes():
    data = request.get_json()
    if data['id'] in recipes:
        recipes[data['id']] = data
        return {
            'recipe updated' : recipes[data['id']]
        }
    return {
        'err' : 'no recipe found with that id'
    }


@app.route('/recipes', methods=["DELETE"])
def del_recipe():
    data = request.get_json()
    if data['id'] in recipes:
        del recipes[data['id']]
        return {
            'recipe gone': f"{data['recipe']} is no more. . . "
        }
    return {
        'err' : "can't delete that recipe, it isn't there "
    }

#post routes

@app.post('/post')
def create_post():
    post_data = request.get_json()
    if post_data['author'] not in recipes:
        return {"message": "recipe does not exist"}, 400
    post_id = uuid4.hex()
    posts[post_id] = post_data
    return {
        'message': "Recipe post created",
        'post-id': post_id
        }, 201

@app.get('/post')
def get_posts():
    try:
        return list(posts.values()), 200
    except:
        return {'message':"Failed to get recipe posts"}, 400

@app.get('/post/<post_id>')
def get_ind_post(post_id):
    try: 
        return posts[post_id], 200
    except KeyError:
        return {'message':"invalid recipe post"}, 400

@app.put('/post')
def update_post():
    post_data = request.get_json()

    if post_data['id'] in posts:
        posts[post_data['id']] = {k:v for k,v in post_data.items() if k != 'id'} 

        return {'message': f'recipe post: {post_data["id"]} updated'}, 201
    
    return {'message': "invalid recipe post"}, 400

@app.delete('/post')
def delete_post():
    post_data = request.get_json()
    post_id = post_data['id']

    if post_id not in posts:
        return { 'message' : "Invalid Recipe Post"}, 400
    
    posts.pop(post_id)
    return {'message': f'Recipe Post: {post_id} deleted'}
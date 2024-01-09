from fastapi import FastAPI, Header, Body

app = FastAPI()

@app.get("/")
def greet():
    # return "Hello? World?"
    return {"message" : "Hello World"}

@app.get('/students/{sname}')
def get_student(sname: str):
    return {'name' : f'Hello {sname}!, I hope you are well'}

# Parameter
@app.get('/{org_name}/students/{sname}')
def get_organization_student(org_name: str, sname: str):
    return {'name' : f'Hello {sname}!, I hope you are well from {org_name}', 'organization' : org_name}

# Query Parameter (Key Value)
@app.get('/student_form/')
def student_form(name:str, email:str):
    return {"name" : name, "email" : email}

#POST -- Header
@app.post('/hi_post')
def greet(who :str =Header()):
    return f"Hello {who}!"

#POST -- Body
@app.post('/hi_post_body')
def greet(who :str =Body()):
    return f"Hello {who}!"

@app.post('/hi_post_body_json')
def greet(who :str =Body(embed=True)):
    return f"Hello {who}!"

from model import Creature
from data import get_creatures
@app.get('/creatures')
def get_all() -> list[Creature]:
    return get_creatures()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('hello:app', reload=True)

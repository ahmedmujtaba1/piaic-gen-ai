from fastapi import FastAPI

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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('hello:app', reload=True)

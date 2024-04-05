import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
def index():
    return {'message': 'Welcome to Contacts Application'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='localhost', port=8000, reload=True
    )

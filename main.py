import fastapi
import uvicorn

import fastapi.middleware.cors as cors
import sqlalchemy as sqa
import sqlalchemy.ext.asyncio as asyncio

import src.db as db
# from src.contacts import routes as contacts_routes
from src.auth import routes as auth_routes


app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/api")
# app.include_router(contacts.router, prefix="/api")


@app.get('/')
def index():
    return {'message': 'Welcome to Contacts Application'}


@app.get("/api/healthchecker")
async def healthchecker(db: asyncio.AsyncSession = fastapi.Depends(db.get_db)):
    try:
        # Make request
        result = await db.execute(sqa.text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise fastapi.HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise fastapi.HTTPException(status_code=500, detail="Error connecting to the database")


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='localhost', port=8000, reload=True
    )

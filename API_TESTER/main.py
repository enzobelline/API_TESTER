from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from API_TESTER.routes import auth, protected

def create_api():
    app = FastAPI()
    
    # Rate limiter
    limiter = Limiter(key_func=get_remote_address)
    app.state.limiter = limiter

    # Include routes
    app.include_router(auth.router)
    app.include_router(protected.router)

    return app

app = create_api()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("yourlibrary.main:app", host="0.0.0.0", port=8000, reload=True)

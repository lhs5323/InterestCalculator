import uvicorn
from os.path import abspath
import pathlib as path
from starlette.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Response
from routers.main_router import router as main_router

app = FastAPI(title='sunghwa-interest-rate-API', version='0.0.1', docs_url=None, redoc_url=None)
app.include_router(main_router)

@app.middleware('http')
async def add_cors(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

static_folder = abspath(path.Path(path.Path(__file__).parent.absolute() ,'..', 'static'))
app.mount("/", StaticFiles(directory="../static", html=True), name='static')

if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0', port=8000, reload=True)
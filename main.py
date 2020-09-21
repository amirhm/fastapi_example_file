import fastapi
from pydantic import BaseModel
from fastapi import File, UploadFile
from fastapi.responses import StreamingResponse

d = []

class cmd(BaseModel):
    cmd:str = 'test'
    param:str = 'f'

app = fastapi.FastAPI()
files = {'file': open('client.py', 'rb')}

@app.get('/')
def main():
    return {'answer':'OK'}

@app.get('/rcv')
def send_data(idx:int):
    
    return {'first entry':d[idx].cmd,'second entry':d[idx].param}

@app.post('/cmd')
def receive_cmd(f:cmd):
    d.append(f)
    breakpoint()
    return {'first entry':f.cmd,'second entry':f.param}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    print(contents)
    return {"filename": file.filename}

@app.get("/getfile/")
async def send_file():
    print('test')
    file_like = open('Untitled.mp4','rb')
    return StreamingResponse(file_like, media_type="video/mp4")

from fastapi.responses import FileResponse
@app.get("/getfile2/")
async def get_file():
    print('test')
#    file_like = open('Untitled.mp4','rb')
    return FileResponse('Untitled.mp4')

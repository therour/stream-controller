# Live Streaming Camera API

Camera Routes (`/camera`) are to manage camera data,
while Streaming


## How to run
1. Install dependency
```
pip install -r requirements.txt
```

2. Start Server
```
uvicorn app.main:app
```

3. Open API Docs (Swaggger) on http://localhost:3000/docs


### Docker
1. Build image
```
docker build -t streaming .
```

2. Start container
```
docker run -p 3000:3000 streaming
```

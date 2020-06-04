# Dockerコンテナ起動

```
docker run -itd --name yuki -p 8000:8000 test /bin/sh
```


# Dockerの中に入る

```
docker exec -it yuki /bin/bash
```

# Gunicorn起動

```
gunicorn --bind 0.0.0.0 app:app -w 4 -k uvicorn.workers.UvicornWorker
```
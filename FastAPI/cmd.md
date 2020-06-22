# Dockerコンテナ起動

```
docker run -itd --name yuki -p 8000:8000 test /bin/sh
```

# 起動2

```
docker run -d --name yuki -p 8000:8000 test
```

# Dockerの中に入る

```
docker exec -it yuki /bin/bash
```

# Gunicorn起動

```
gunicorn --bind 0.0.0.0 app:app -w 4 -k uvicorn.workers.UvicornWorker
```

```
gunicorn --bind 0.0.0.0 app:app --workers 1 --threads 8 -k uvicorn.workers.UvicornWorker
```
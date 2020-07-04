# Dockerコンテナ起動

```
docker run -itd --name yuki -v app:/app -p 8000:8000 test /bin/sh
```

# Dockerの中に入る

```
docker exec -it yuki /bin/bash
```

# volume

```
docker run --volume $PWD/app:/app -itd --name=yuki test
```
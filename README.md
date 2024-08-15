# Развертывание gRPC-сервиса в Yandex DataSphere на основе Docker-образа

Пример содержит простейший Docker-образ для развертывания gRPC-сервиса в Yandex DataSphere. Сервис предусматривает проверки работоспособности образа и отправляет метрики в формате Prometheus. 

## Как собрать Docker-образ

Установите Docker. В командной оболочке выполните следующие команды:

```
docker build --platform linux/amd64 -t grpc-server .
docker tag grpc-server <docker_repo_with_tag>
docker push <docker_repo_with_tag>
```

Подробное руководство см. в [документации Yandex Cloud](https://cloud.yandex.ru/ru/docs/datasphere/tutorials/grpc-node).

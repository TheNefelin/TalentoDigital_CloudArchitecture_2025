## **3. CloudShell**:
### Consola CloudShell
- Subir el archivo comprimido `FinTechPlusApi.zip`
```sh
ls
ls -a
```
```sh
unzip FinTechPlusApi.zip
```
```sh
cd FinTechPlusApi
```

- Utilizar los comandos `View push commands` de `fin-tech-plus-repo` para crear la imagen docker en el repositorio.
```sh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123.dkr.ecr.us-east-1.amazonaws.com
```
```sh
docker build -t fin-tech-plus-repo .
```
```sh
docker tag fin-tech-plus-repo:latest 123.dkr.ecr.us-east-1.amazonaws.com/fin-tech-plus-repo:latest
```
```sh
docker push 123.dkr.ecr.us-east-1.amazonaws.com/fin-tech-plus-repo:latest
```

### Limpiar CloudShell
- Listas de imagenes
```sh
docker images
```
- Eliminar imagen específica
```sh
docker rmi [id]
```
- Limpieza completa de Docker
```sh
df -h
```
```sh
docker system prune -af
docker volume prune -f
```
```sh
rm -f FinTechPlusApi.zip
rm -rf FinTechPlusApi/
```

---


# aso-git-webapp

1) Construir la imagen en local y ejecutarla para ver que todo es correcto
Cuidado con las variables de entorno ;)
```
docker build
docker run (con cosas aquí)
```

2a) Construir la imagen con gcloud build y publicarla en cloud artifact registry
```
gcloud submit .... cosas ...
```

2b) Construir la imagen en local, etiquetarla para cloud articfact y subirla
```
docker build . -t etiqueta_especial
docker push etiqueta_especial
```

3) Crear un servicio de Cloud Run a partir de esa imagen
Cuidado, no copy/paste lo siguiente, que literalmente no os funcionará
```
gcloud run deploy webapp --image=europe-west1-docker.pkg.dev/aso-git/webapp/webapp:gcp
```

4) Probar que todo funciona

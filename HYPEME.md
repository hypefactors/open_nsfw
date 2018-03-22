# How to use

This simply adds a small python web service inside a docker image.

The service accepts post requests uploading images and then runs the open\_nsfw classifier on them. 
It responds with the classification result (i.e. `0.56`).

While the service can be run in parallel, no effort is made to avoid file name clashes. This is left as the responsibility of the caller.

Build the docker image like this: 
```
docker build -t my_image .
```

then run it like this: 
```
docker run -p 4000:80 my_image
```

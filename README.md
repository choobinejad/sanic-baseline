# sanic-baseline

A baseline project that includes:
- A web service with authentication, CORS, xss headers, and a Swagger UI
- A sample client for the web service
- A celery-flavored backend
- environment files (docker, virtualenv, requirements)
- RTD-themed docs

\#workInProgress. Cache and authorization need some work to make them intuitive, 
transparent, and pluggable. Config is pretty lame -- need to implement a more
dynamic system that will pick up env variables. and reload configs when needed.
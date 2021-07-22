# Remote ID
This folder contains API definitions for remote ID consistent with the
ASTM remote ID standard.  `canonical.yaml` attempts to represent the
specifications of the standard as directly as possible while
`augmented.yaml` adds optional extensions that implementers have found useful.

## Viewing locally
To view this YAML file locally:

```shell script
docker run -it --rm -p 8080:8080 \
  -v $(pwd)/canonical.yaml:/usr/share/nginx/html/swagger.yaml \
  -e PORT=8080 -e SPEC_URL=swagger.yaml redocly/redoc
```

...then visit [http://localhost:8080/](http://localhost:8080/) in a browser.

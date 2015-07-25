# Millipede as a Service

## About

API to generate millipedes

## Documentation

`GET /api/\<version\>/millipede`
* return: a millipede
* parameters:
    * size: provide the size of the millipede (default is 10)
    * reverse: true to have a reverse millipede (default is false)
    * comment: provide a comment to the generated millipede

## Configuration

By default MaaS looks for an optional configuration file located to `/etc/maas.cfg`.
You can override this value by setting the environment variable `MAAS_CONFIG_FILE` to whatever it pleases.

The configuration file expected content is valid python code.

### Values:
* `REDIS_URL`: Url to the redis server for cache purpose. Caching is optional but greatly recommended

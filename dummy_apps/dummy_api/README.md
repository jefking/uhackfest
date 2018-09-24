# Dummy API
This is a dummy API in the place of our internal APIs, called by the processors. We store our secrets elsewhere, but for this dummy the credentials are hardcoded as *user/pass*.

Run `make run` to run the container.

## Dependencies
make, docker.


## API Endpoints

**GET /healthcheck**

Does not require authentication. Returns a hardcoded JSON response.

**GET /secret**

Requires authentication. Returns a hardcoded JSON response.

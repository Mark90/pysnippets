# PySnippets

This repository will be an archive to any Python snippets I write that are not big enough for another repository.
The purpose of these scripts vary; sometimes I want to learn about a pypi package or a module from the standard library.
I also want to do benchmarking different solutions to a problem in terms of execution times or memory usage.
Other purposes are to prototype ideas I have, or document how I got certain things done.

## Running with Docker

Install Docker Machine for your distribution.

Build the image:

```commandline
git clone https://github.com/Mark90/pysnippets
cd pysnippets
docker build -t pysnippets .
```

Run scripts in a container for the image:
```commandline
docker run -it --rm --name pysnippets_container pysnippets python stdlib/functools/lru_cache/benchmarks.py
```

Better command, mounts a volume so that you don't need to rebuild the image every time.

```
docker run -it --rm --name pysnippets_container -v "$PWD/src":/app pysnippets python stdlib/functools/lru_cache/benchmarks.py
```

### Integrating PyCharm

You will also need Docker Compose installed for this.

#### Docker configuration
Then in PyCharm's settings, go to *Build, Execution, Deployment > Docker* and add a Docker server
with these settings:

```
API URL: unix:///var/run/docker.sock
Docker Compose Executable: docker-compose
CHECK - Import credentails from Docker Machine
```

#### Remote Python interpreter in Docker
 
Go to *Project > Project Interpreter* and click to the right of *Project Interpreter* and
 *Add Remote*, then supply this configuration:

```
Name: Remote Python 3.6.1 Docker (pysnippets:latest)
CHECK - Docker
Server: Docker (the one you just created)
Image name: pysnippets:latest
Python interpreter path: python (should be all you need)
```

#### Create a run configuration

PyCharm run configuration example for pysnippets/stdlib/functools/lru_cache/benchmarks.py;

```
Script: benchmarks.py
Script parameters: <empty>

Project: pysnippets
Environment variables: PYTHONUNBUFFERED=1
Python interprter: Project Default (Remote Python 3.6.1 Docker (pysnippets:latest))
Interpreter options: <empty>
Working directory: /app/stdlib/functools/lru_cache
Path mappings: <empty>
```

We have defined PYTHONPATH in the dockerfile to let python know where our modules live. By default, 
PyCharm will complement this environment variable with the content and source roots. But in the case of
running in a Docker container it _overwrites_ the variable instead of appending to it, so we need to 
uncheck *Add content roots to PYTHONPATH* and *Add source roots to PYTHONPATH*.


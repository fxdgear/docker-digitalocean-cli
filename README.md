# docker-digitalocean-cli
Digital Ocean CLI in a Container

Really simple CLI client to communicate to the Digital Ocean API. Runs inside a container. 

This is mostly just me goofiing off with docker and DO's API. 

It's highly recomended that you create an alias: 
First login to Digital Ocean and create an API token.
Second create the alias:

```bash
alias do='docker run -it --rm -v /home/nick/Documents/docker-fundamentals/do_utilities:/app/ -e "ACCESS_TOKEN=<your DO access token>" fxdgear/docker-digitalocean-cli'
```

Once this is complete you can run `do` to see a list of arguments. 

```bash
$ do
usage: do.py [-h] [-l] [--create-docker-vm] [--list-regions] [--list-droplets]
             [--destroy-droplet] [-n COUNT] [-r REGION] [-s SIZE] [-a]
             [ID [ID ...]]

Digital Ocean Helper

positional arguments:
  ID

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list images
  --create-docker-vm    Create Docker Image
  --list-regions        List regions
  --list-droplets       List Dropletss
  --destroy-droplet     Destroy Droplets
  -n COUNT, --count COUNT
  -r REGION, --region REGION
  -s SIZE, --size SIZE
  -a, --all
```

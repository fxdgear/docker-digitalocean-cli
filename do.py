import os
import pyocean

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
do = pyocean.DigitalOcean(ACCESS_TOKEN)


def get_images():
    return do.image.all()


def get_docker_image():
    images = get_images()
    for image in images:
        if image.slug == 'docker':
            return image


def list_images(args):
    for image in get_images():
        print image


def list_regions(args):
    for region in do.region.all():
        print "{name}: {slug} {sizes}".format(
            name=getattr(region, 'name'),
            slug=getattr(region, 'slug'),
            sizes=getattr(region, '_attrs')['sizes'],
        )


def get_droplets():
    return do.droplet.all()


def list_droplets(args):
    for droplet in get_droplets():
        print("{name}: {id}".format(name=droplet.name, id=droplet.id))


def destroy_droplet(args):
    destroy_all = getattr(args, 'all')
    droplets = get_droplets()
    droplets_to_destroy = []
    droplet_ids = getattr(args, 'ids')
    if destroy_all:
        droplets_to_destroy = droplets
    else:
        for droplet in droplets:
            if droplet.id in droplet_ids:
                droplets_to_destroy.append(droplet)
    for droplet in droplets_to_destroy:
        print "Destroying droplet: {}".format(droplet.name)
        droplet.destroy()


def create_docker_vm(args):
    docker_image = get_docker_image()
    count = getattr(args, 'count')
    region = getattr(args, 'region')
    size = getattr(args, 'size')
    image = getattr(docker_image, 'slug')
    for c in xrange(count):
        name = 'introtodocker-{}'.format(c)
        print("Creating image: {}".format(name))
        attrs = {
            'name': name,
            'region': region,
            'size': size,
            'image': image,
        }
        do.droplet.create(attrs)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Digital Ocean Helper")
    parser.add_argument(
        '-l', '--list',
        dest='action',
        action='store_const',
        const=list_images,
        help='list images'
    )
    parser.add_argument(
        '--create-docker-vm',
        dest='action',
        action='store_const',
        const=create_docker_vm,
        help='Create Docker Image'
    )
    parser.add_argument(
        '--list-regions',
        dest='action',
        action='store_const',
        const=list_regions,
        help='List regions',
    )
    parser.add_argument(
        '--list-droplets',
        dest='action',
        action='store_const',
        const=list_droplets,
        help='List Dropletss',
    )
    parser.add_argument(
        '--destroy-droplet',
        dest='action',
        action='store_const',
        const=destroy_droplet,
        help='Destroy Droplets',
    )

    parser.add_argument('-n', '--count', type=int, default=1)
    parser.add_argument('-r', '--region', type=str, default='nyc2')
    parser.add_argument('-s', '--size', type=str, default='512mb')
    parser.add_argument('-a', '--all', action='store_true', default=False)
    parser.add_argument('ids', type=int, metavar='ID', nargs='*', default=[])

    args = parser.parse_args()
    if args.action is None:
        parser.parse_args(['-h'])
    args.action(args)

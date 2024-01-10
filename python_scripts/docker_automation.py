import subprocess
import argparse
import logging


def setup_logging():
    logging.basicConfig(
        filename="automation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def automate_build(image_name, dockerfile_path):
    try:
        subprocess.run(
            ["docker", "build", "-t", image_name, dockerfile_path], check=True
        )
        logging.info("Created Image: %s", image_name)

    except subprocess.CalledProcessError as e:
        logging.error("Error: Couldn't build image: %s", str(e))
        raise


def run_container(image_name, name_container):
    try:
        subprocess.run(
            [
                "docker",
                "run",
                "--name",
                name_container,
                "-d",
                "-p",
                "3000:3000",
                image_name,
            ]
        )
        logging.info("Started Docker container: %s", name_container)

    except subprocess.CalledProcessError as e:
        logging.error("Error: Couldn't spin up Docker container: %s", str(e))
        raise


def main():
    setup_logging()
    parser = argparse.ArgumentParser(
        description="Automate build and run for a Dockerized React app."
    )
    parser.add_argument("image_name", type=str, help="Name for the Docker image")
    parser.add_argument("dockerfile_path", type=str, help="Path to the Dockerfile")
    parser.add_argument(
        "name_container", type=str, help="Name for the Docker container"
    )
    parser.add_argument(
        "--rebuild", action="store_true", help="Rebuild the Docker image"
    )

    args = parser.parse_args()

    try:
        if args.rebuild:
            logging.info("Building Image and running container")
            automate_build(args.image_name, args.dockerfile_path)
            run_container(args.image_name, args.name_container)
        else:
            logging.info("Running container")
            run_container(args.image_name, args.name_container)
    except Exception as e:
        logging.exception("An error occurred: %s", str(e))


if __name__ == "__main__":
    main()

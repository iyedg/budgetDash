import click
from loguru import logger


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def main(count, name):
    logger.info("It's working!")
    logger.error(f"Showing your name: {name} {count} times")

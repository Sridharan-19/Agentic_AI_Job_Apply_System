from database.models import Base
from database.session import engine

from agents.search_agent import (
    run_search_agent
)


def initialize_database():

    Base.metadata.create_all(engine)


if __name__ == "__main__":

    initialize_database()

    run_search_agent()
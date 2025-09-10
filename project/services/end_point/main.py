import uvicorn
from project.utilities.logger.logger_info import Logger

logger = Logger.get_logger()


def main():
    try:

        uvicorn.run(
            app="project.services.end_point.app:app",
            host="0.0.0.0",
            port=8000
        )
    except Exception as e:
        logger.error(f"The server crashed because{e}")


if __name__ == '__main__':
    logger.info("start fastapi server")
    main()

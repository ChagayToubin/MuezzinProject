import uvicorn


def main():

        uvicorn.run(
            app="project.services.end_point.app:app",
            host="0.0.0.0",
            port=8000
        )






if __name__ == '__main__':
    main()

    print("end_pont start")
from app.app import init_app

if __name__ == "__main__":
    app = init_app()
    app.run(port=3000, debug=True)

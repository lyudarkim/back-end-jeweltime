from application import create_app


app = create_app()

if __name__ == "__main__":
    # Remember to remove debug=True once the app is in production
    app.run(debug=True)
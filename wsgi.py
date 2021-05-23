from app import  create_app

if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
else:
    gunicorn_app=create_app()


# to run this app: with gunicorn => gunicorn --bind 0.0.0.0:5000 wsgi:gunicorn_app
    # now there we are
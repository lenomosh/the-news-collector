from newsproject import app

if __name__ == '__main__':
    print(app.config.get('API_KEY'))
    app.run()

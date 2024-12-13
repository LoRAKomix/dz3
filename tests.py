def test_app_config():
    config = {
        "appConfig": {
            "appName": "MyWebApp",
            "version": 1.0,
            "database": {
                "host": "localhost",
                "port": 5432,
                "user": "admin",
                "password": "secret"
            },
            "features": {
                "enableLogging": True,
                "maxConnections": 100
            }
        },
        "print": "Application configuration loaded."
    }
    
    assert config["appConfig"]["appName"] == "MyWebApp"
    assert config["appConfig"]["version"] == 1.0
    assert config["appConfig"]["database"]["port"] == 5432
    assert config["appConfig"]["features"]["enableLogging"] is True

def test_calculations():
    calculations = {
        "addition": {
            "operand1": 10,
            "operand2": 25,
            "result": 10 + 25  # Ожидаемый результат
        },
        "subtraction": {
            "operand1": 50,
            "operand2": 15,
            "result": 50 - 15  # Ожидаемый результат
        }
    }
    
    assert calculations["addition"]["result"] == 35
    assert calculations["subtraction"]["result"] == 35

if __name__ == "__main__":
    test_app_config()
    test_calculations()
    print("All tests passed!")

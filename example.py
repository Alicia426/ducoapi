import ducoapi

api_connection = ducoapi.api_actions()

api_connection.login(username='yourusername', password='yourpass')

current_balance = api_connection.balance()
print(current_balance)

api_connection.close()
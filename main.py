from fire_and_forget.client import Client

if __name__ == '__main__':
    client = Client()
    client.import_csv('test.csv')

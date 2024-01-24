import requests 

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    
    categories = r.json()
    for categori in categories:
        x = f'Estas son las categorias: ' + categori['name']
        print(x)
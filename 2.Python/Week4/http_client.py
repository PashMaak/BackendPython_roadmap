import httpx

URL = "https://jsonplaceholder.typicode.com"

def get_users():
    r = httpx.get(f'{URL}/users')
    print("Executed" if r.status_code//100 == 2 else f"Error {r.status_code}")
    return r.json()
    
def create_user(data):
    r = httpx.post(f'{URL}/users', json=data)
    print("Executed" if r.status_code//100 == 2 else f"Error {r.status_code}")
    return r.json()
    

def delete_user(id):
    r = httpx.delete(f'{URL}/users/{id}')
    print("Executed" if r.status_code//100 == 2 else f"Error {r.status_code}")
    return r.json()


print(get_users())

print(create_user({
    "name": "Anush",
    "username": "anush",
    "email": "anush@example.com"
}))

print(delete_user(1))
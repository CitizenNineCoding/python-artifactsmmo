from dotenv import dotenv_values

cvars = {**dotenv_values(".env.secret"), **dotenv_values(".env.shared")}

if "BEARER_TOKEN" not in cvars.keys():
    raise ValueError("Bearer token missing from env secret file")

headers = {
    'Accept': 'application/json', 
    'Content-Type': 'application/json'
}

auth_header = {'Authorization': f'Bearer {cvars['BEARER_TOKEN']}'}
cvars.pop('BEARER_TOKEN')
cvars.update({'headers': headers, 'auth_header': auth_header})

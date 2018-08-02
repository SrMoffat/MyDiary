const uri = 'http://127.0.0.1:5000/api/v2'

export const api = {
    post (endpoint, data, token=null) {
        return fetch(`${uri}${endpoint}`, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                "x-access-token": token,
                "content-type": "application/json"
            }
        })
    },
    update(endpoint, data=null, token) {
        return fetch(`${uri}${endpoint}`, {
            method: 'PUT',
            body: JSON.stringify(data),
            headers: {
                "x-access-token": token,
                "content-type": "application/json"
            }
        })
    },
    get(endpoint, token) {
        return fetch(`${uri}${endpoint}`, {
            method: 'GET',
            headers: {
                "x-access-token": token,
                "content-type": "application/json"
            }
        })
    },
    delete(endpoint, token) {
        return fetch(`${uri}${endpoint}`, {
            method: 'DELETE',
            headers: {
                "x-access-token": token,
                "content-type": "application/json"
            }
        })
    }
}
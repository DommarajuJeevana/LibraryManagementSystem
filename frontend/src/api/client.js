export const API = 'http://127.0.0.1:8000/api';

export const headers = () => ({
    Authorization: `Token ${localStorage.getItem('token')}`,
    'Content-Type': 'application/json'
});

export async function api(path, opts = {}) {
    const r = await fetch(API + path, {
        ...opts,
        headers: {
            ...headers(),
            ...(opts.headers || {})
        }
    });

    const data = await r.json().catch(() => ({}));

    if (!r.ok) {
        throw new Error(data.detail || 'Request failed');
    }

    return data;
}
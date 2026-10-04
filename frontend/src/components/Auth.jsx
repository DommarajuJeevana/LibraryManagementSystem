import React, { useState } from 'react';
import { API } from '../api/client';

export default function Auth({ onLogin }) {
    const [register, setRegister] = useState(false);
    const [f, setF] = useState({
        username: '',
        password: '',
        first_name: '',
        last_name: '',
        email: '',
        phone: ''
    });
    const [err, setErr] = useState('');

    const set = (k, v) => setF({ ...f, [k]: v });

    const submit = async e => {
        e.preventDefault();
        setErr('');

        try {
            const d = await fetch(
                `${API}/auth/${register ? 'register' : 'login'}/`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(f)
                }
            ).then(async r => {
                const x = await r.json();

                if (!r.ok) {
                    throw Error(x.detail);
                }

                return x;
            });

            localStorage.setItem('token', d.token);
            onLogin(d.user);
        } catch (e) {
            setErr(e.message);
        }
    };

    return (
        <div className="auth">
            <div className="auth-card">
                <h1>📚 Library Management</h1>
                <p>
                    {register
                        ? 'Create your member account'
                        : 'Sign in to continue'}
                </p>

                <form onSubmit={submit}>
                    {register && (
                        <>
                            <input
                                placeholder="First name"
                                value={f.first_name}
                                onChange={e =>
                                    set('first_name', e.target.value)
                                }
                            />

                            <input
                                placeholder="Last name"
                                value={f.last_name}
                                onChange={e =>
                                    set('last_name', e.target.value)
                                }
                            />

                            <input
                                placeholder="Email"
                                value={f.email}
                                onChange={e =>
                                    set('email', e.target.value)
                                }
                            />

                            <input
                                placeholder="Phone"
                                value={f.phone}
                                onChange={e =>
                                    set('phone', e.target.value)
                                }
                            />
                        </>
                    )}

                    <input
                        required
                        placeholder="Username"
                        value={f.username}
                        onChange={e =>
                            set('username', e.target.value)
                        }
                    />

                    <input
                        required
                        type="password"
                        placeholder="Password"
                        value={f.password}
                        onChange={e =>
                            set('password', e.target.value)
                        }
                    />

                    {err && <div className="error">{err}</div>}

                    <button>
                        {register ? 'Register' : 'Login'}
                    </button>
                </form>

                <button
                    className="link"
                    onClick={() => setRegister(!register)}
                >
                    {register
                        ? 'Already have an account? Login'
                        : 'New member? Register'}
                </button>

                {!register && (
                    <small>Demo admin: admin / Admin@123</small>
                )}
            </div>
        </div>
    );
}
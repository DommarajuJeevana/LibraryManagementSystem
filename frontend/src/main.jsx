import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

import Auth from './components/Auth';
import { api } from './api/client';
import Books from './modules/vengasree/Books';
import Members from './modules/mounika/Members';
import Search from './modules/gagana/Search';
import IssueReturn from './modules/jeevana/IssueReturn';
import Dashboard from './modules/madhupriya/Dashboard';
import Reports from './modules/madhupriya/Reports';

function App() {
    const [user, setUser] = useState(null),
        [page, setPage] = useState('dashboard'),
        [msg, setMsg] = useState('');

    useEffect(() => {
        if (localStorage.getItem('token')) {
            api('/auth/me/')
                .then(setUser)
                .catch(() => localStorage.removeItem('token'));
        }
    }, []);

    if (!user) return <Auth onLogin={setUser}/>;

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
    };

    const items = [
        ['dashboard', 'Dashboard'],
        ...(user.is_staff ? [
            ['books', 'Book Management'],
            ['members', 'Member Management'],
            ['issue', 'Issue / Return'],
            ['reports', 'Transactions / Reports']
        ] : []),
        ['search', 'Search & Availability']
    ];

    return (
        <div className="app">
            <aside>
                <h2>📚 LMS</h2>

                <div className="user">{user.name}</div>

                {items.map(([id, n]) => (
                    <button
                        key={id}
                        className={page === id ? 'active' : ''}
                        onClick={() => {
                            setPage(id);
                            setMsg('');
                        }}
                    >
                        {n}
                    </button>
                ))}

                <button className="logout" onClick={logout}>
                    Logout
                </button>
            </aside>

            <main>
                <header>
                    <h1>
                        {items.find(x => x[0] === page)?.[1]}
                    </h1>

                    {msg && <div className="success">{msg}</div>}
                </header>

                {page === 'dashboard' && <Dashboard />}
                {page === 'books' && <Books setMsg={setMsg} />}
                {page === 'members' && <Members setMsg={setMsg} />}
                {page === 'search' && <Search />}
                {page === 'issue' && (
                    <IssueReturn setMsg={setMsg} />
                )}
                {page === 'reports' && <Reports />}
            </main>
        </div>
    );
}

createRoot(document.getElementById('root')).render(<App />);
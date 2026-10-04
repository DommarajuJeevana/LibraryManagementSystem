import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';

export default function Dashboard() {
    const [data, setData] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        api('/dashboard/')
            .then(setData)
            .catch(err => setError(err.message));
    }, []);

    if (error) {
        return (
            <div className="card">
                Error loading dashboard: {error}
            </div>
        );
    }

    if (!data) {
        return (
            <div className="card">
                Loading dashboard...
            </div>
        );
    }

    const cards = [
        ['Total Books', data.total_books],
        ['Total Copies', data.total_copies],
        ['Available Copies', data.available_copies],
        ['Total Members', data.total_members],
        ['Active Issues', data.active_issues],
        ['Returned Books', data.returned],
    ];

    return (
        <div>
            <h2>Library Dashboard</h2>

            <div className="grid">
                {cards.map(([label, value]) => (
                    <div className="card" key={label}>
                        <h3>{label}</h3>
                        <p>{value}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
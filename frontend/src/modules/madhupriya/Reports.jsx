import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';

export default function Reports() {
    const [transactions, setTransactions] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        api('/reports/')
            .then(data => setTransactions(data.transactions || []))
            .catch(err => setError(err.message));
    }, []);

    if (error) {
        return (
            <div className="card">
                Error loading reports: {error}
            </div>
        );
    }

    return (
        <div>
            <h2>Transactions / Reports</h2>

            {transactions.length === 0 ? (
                <div className="card">
                    No transactions found.
                </div>
            ) : (
                <div className="card">
                    <table>
                        <thead>
                            <tr>
                                <th>Book</th>
                                <th>Member</th>
                                <th>Issue Date</th>
                                <th>Return Date</th>
                                <th>Status</th>
                            </tr>
                        </thead>

                        <tbody>
                            {transactions.map(tx => (
                                <tr key={tx.id}>
                                    <td>{tx.book_title}</td>
                                    <td>{tx.member_name}</td>
                                    <td>{tx.issue_date}</td>
                                    <td>{tx.return_date || '-'}</td>
                                    <td>{tx.status}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
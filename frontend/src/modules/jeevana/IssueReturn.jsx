import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';
import Table from '../../components/Table';

export default function IssueReturn({ setMsg }) {
    const [books, setBooks] = useState([]),
        [members, setMembers] = useState([]),
        [tx, setTx] = useState([]),
        [book, setBook] = useState(''),
        [member, setMember] = useState('');

    const load = () =>
        Promise.all([
            api('/books/'),
            api('/members/'),
            api('/transactions/')
        ]).then(([b, m, t]) => {
            setBooks(b);
            setMembers(m);
            setTx(t);
        });

    useEffect(load, []);

    const issue = async () => {
        try {
            await api('/transactions/', {
                method: 'POST',
                body: JSON.stringify({
                    book_id: book,
                    member_id: member
                })
            });
            setMsg('Book issued successfully');
            setBook('');
            load();
        } catch (e) {
            setMsg(e.message);
        }
    };

    const ret = async id => {
        try {
            await api(`/transactions/${id}/return/`, {
                method: 'POST'
            });
            setMsg('Book returned successfully');
            load();
        } catch (e) {
            setMsg(e.message);
        }
    };

    return (
        <>
            <div className="panel">
                <h2>Issue Book</h2>
                <div className="form-row">
                    <select
                        value={book}
                        onChange={e => setBook(e.target.value)}
                    >
                        <option value="">Select available book</option>
                        {books
                            .filter(b => b.available_copies > 0)
                            .map(b => (
                                <option value={b.id} key={b.id}>
                                    {b.title} ({b.available_copies})
                                </option>
                            ))}
                    </select>

                    <select
                        value={member}
                        onChange={e => setMember(e.target.value)}
                    >
                        <option value="">Select member</option>
                        {members
                            .filter(m => m.active)
                            .map(m => (
                                <option value={m.id} key={m.id}>
                                    {m.name}
                                </option>
                            ))}
                    </select>

                    <button
                        disabled={!book || !member}
                        onClick={issue}
                    >
                        Issue
                    </button>
                </div>
            </div>

            <Table
                rows={tx}
                cols={[
                    'book_title',
                    'member_name',
                    'issue_date',
                    'return_date',
                    'status'
                ]}
                action={t =>
                    t.status === 'ISSUED' ? (
                        <button onClick={() => ret(t.id)}>
                            Return
                        </button>
                    ) : null
                }
            />
        </>
    );
}
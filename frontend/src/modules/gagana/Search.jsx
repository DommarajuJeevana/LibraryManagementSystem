import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';
import Table from '../../components/Table';

export default function Search() {
    const [q, setQ] = useState('');
    const [books, setBooks] = useState([]);

    const go = () => {
        api(`/books/?search=${encodeURIComponent(q)}`).then(setBooks);
    };

    useEffect(go, []);

    return (
        <>
            <div className="panel form-row">
                <input
                    placeholder="Search title, author, ISBN or category"
                    value={q}
                    onChange={e => setQ(e.target.value)}
                    onKeyDown={e => e.key === 'Enter' && go()}
                />

                <button onClick={go}>
                    Search
                </button>
            </div>

            <Table
                rows={books}
                cols={[
                    'title',
                    'author',
                    'isbn',
                    'category',
                    'available_copies',
                    'availability'
                ]}
            />
        </>
    );
}
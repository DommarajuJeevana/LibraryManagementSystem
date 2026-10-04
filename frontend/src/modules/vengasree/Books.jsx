import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';
import Table from '../../components/Table';

export default function Books({ setMsg }) {
    const [books, setBooks] = useState([]);

    const [f, setF] = useState({
        title: '',
        author: '',
        isbn: '',
        category: '',
        total_copies: 1
    });

    const load = () => api('/books/').then(setBooks);

    useEffect(load, []);

    const add = async (e) => {
        e.preventDefault();

        try {
            await api('/books/', {
                method: 'POST',
                body: JSON.stringify({
                    ...f,
                    total_copies: +f.total_copies,
                    available_copies: +f.total_copies
                })
            });

            setF({
                title: '',
                author: '',
                isbn: '',
                category: '',
                total_copies: 1
            });

            setMsg('Book added successfully');
            load();
        } catch (e) {
            setMsg(e.message);
        }
    };

    const del = async (id) => {
        if (confirm('Delete this book?')) {
            try {
                await api(`/books/${id}/`, {
                    method: 'DELETE'
                });

                setMsg('Book deleted');
                load();
            } catch (e) {
                setMsg(e.message);
            }
        }
    };

    return (
        <>
            <div className="panel">
                <h2>Add Book</h2>

                <form className="form-row" onSubmit={add}>
                    {['title', 'author', 'isbn', 'category'].map((k) => (
                        <input
                            key={k}
                            required
                            placeholder={k.replace('_', ' ')}
                            value={f[k]}
                            onChange={(e) =>
                                setF({ ...f, [k]: e.target.value })
                            }
                        />
                    ))}

                    <input
                        type="number"
                        min="1"
                        placeholder="copies"
                        value={f.total_copies}
                        onChange={(e) =>
                            setF({ ...f, total_copies: e.target.value })
                        }
                    />

                    <button>Add</button>
                </form>
            </div>

            <Table
                rows={books}
                cols={[
                    'title',
                    'author',
                    'isbn',
                    'category',
                    'total_copies',
                    'available_copies',
                    'availability'
                ]}
                action={(b) => (
                    <button
                        className="danger"
                        onClick={() => del(b.id)}
                    >
                        Delete
                    </button>
                )}
            />
        </>
    );
}
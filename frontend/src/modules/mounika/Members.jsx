import React, { useEffect, useState } from 'react';
import { api } from '../../api/client';
import Table from '../../components/Table';

export default function Members({ setMsg }) {
    const [members, setMembers] = useState([]);

    const [f, setF] = useState({
        username: '',
        password: 'Member@123',
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        address: ''
    });

    const load = () => api('/members/').then(setMembers);

    useEffect(load, []);

    const add = async (e) => {
        e.preventDefault();

        try {
            await api('/members/', {
                method: 'POST',
                body: JSON.stringify(f)
            });

            setF({
                username: '',
                password: 'Member@123',
                first_name: '',
                last_name: '',
                email: '',
                phone: '',
                address: ''
            });

            setMsg('Member added successfully');
            load();
        } catch (e) {
            setMsg(e.message);
        }
    };

    const del = async (id) => {
        if (confirm('Delete this member?')) {
            try {
                await api(`/members/${id}/`, {
                    method: 'DELETE'
                });

                setMsg('Member deleted');
                load();
            } catch (e) {
                setMsg(e.message);
            }
        }
    };

    return (
        <>
            <div className="panel">
                <h2>Add Member</h2>

                <form className="form-row" onSubmit={add}>
                    <input
                        required
                        placeholder="username"
                        value={f.username}
                        onChange={(e) =>
                            setF({ ...f, username: e.target.value })
                        }
                    />

                    <input
                        required
                        placeholder="first name"
                        value={f.first_name}
                        onChange={(e) =>
                            setF({ ...f, first_name: e.target.value })
                        }
                    />

                    <input
                        placeholder="last name"
                        value={f.last_name}
                        onChange={(e) =>
                            setF({ ...f, last_name: e.target.value })
                        }
                    />

                    <input
                        placeholder="phone"
                        value={f.phone}
                        onChange={(e) =>
                            setF({ ...f, phone: e.target.value })
                        }
                    />

                    <input
                        placeholder="address"
                        value={f.address}
                        onChange={(e) =>
                            setF({ ...f, address: e.target.value })
                        }
                    />

                    <button>Add</button>
                </form>
            </div>

            <Table
                rows={members}
                cols={[
                    'name',
                    'phone',
                    'address',
                    'joined_date',
                    'active'
                ]}
                action={(m) => (
                    <button
                        className="danger"
                        onClick={() => del(m.id)}
                    >
                        Delete
                    </button>
                )}
            />
        </>
    );
}
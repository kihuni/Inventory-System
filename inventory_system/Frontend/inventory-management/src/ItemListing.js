import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ItemListing.css';
import CreateItemForm from './createItem'; 

const ItemListing = ({ isActive }) => { 
    const [items, setItems] = useState([]);
    const [showCreateForm, setShowCreateForm] = useState(false);

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/inventory/items/');
                setItems(response.data);
            } catch (error) {
                console.error('Error fetching items:', error);
            }
        };

        fetchItems();
    }, []);

    if (!isActive) return null;

    return (
        <div className="item-listing-container"> 
            {showCreateForm ? (
                <>
                    <CreateItemForm />
                    <button onClick={() => setShowCreateForm(false)}>Cancel</button>
                </>
            ) : (
                <>
                    <button className="create-item-button" onClick={() => setShowCreateForm(true)}>Create Item</button>
                    <h1>Item List</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Description</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Image</th>
                            </tr>
                        </thead>
                        <tbody>
                            {items.map((item) => (
                                <tr key={item.id}>
                                    <td>{item.name}</td>
                                    <td>{item.description}</td>
                                    <td>{item.price}</td>
                                    <td>{item.quantity}</td>
                                    <td>
                                        <img src={item.image} alt={item.name} />
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </>
            )}
        </div>
    );
};

export default ItemListing;

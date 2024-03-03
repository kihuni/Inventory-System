import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ItemListing.css'; 

const ItemListing = ({ isActive }) => { // Pass isActive prop to control rendering
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const response = await axios.get('http://localhost:8000/inventory/items');
                setItems(response.data);
            } catch (error) {
                console.error('Error fetching items:', error);
            }
        };

        fetchItems();
    }, []);

    // Conditionally render based on isActive prop
    if (!isActive) return null;

    return (
        <div className="item-listing-container"> {/* Apply container class */}
            <h1>Item Listing</h1>
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
        </div>
    );
};

export default ItemListing;

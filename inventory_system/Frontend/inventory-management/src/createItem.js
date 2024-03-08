import React, { useState } from 'react';
import axios from 'axios';
import './createItem.css';

const CreateItemForm = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [price, setPrice] = useState('');
    const [quantity, setQuantity] = useState('');
    const [image, setImage] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/inventory/items/', {
            name,
            description,
            price,
            quantity,
            image
        })
        .then(response => {
            // Handle successful response
            console.log(response.data);
        })
        .catch(error => {
            // Handle error
            console.error(error);
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="name">Name:</label>
            <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} />

            <label htmlFor="description">Description:</label>
            <textarea id="description" value={description} onChange={(e) => setDescription(e.target.value)} />

            <label htmlFor="price">Price:</label>
            <input type="number" id="price" value={price} onChange={(e) => setPrice(e.target.value)} />

            <label htmlFor="quantity">Quantity:</label>
            <input type="number" id="quantity" value={quantity} onChange={(e) => setQuantity(e.target.value)} />

            <label htmlFor="image">Image:</label>
            <input type="file" id="image" onChange={(e) => setImage(e.target.files[0])} />

            <button type="submit">Create Item</button>
        </form>
    );
};

export default CreateItemForm;
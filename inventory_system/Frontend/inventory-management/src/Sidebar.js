import React, { useState } from "react";
import Header from "./Header";
import ItemListing from "./ItemListing";
import './Sidebar.css';

const Sidebar = () => {
    const [activeComponent, setActiveComponent] = useState('dashboard'); // State to track active component

    return (
        <div className="sidebar">
            <Header />
            <ul>
                <li>
                    <a href="#" onClick={() => setActiveComponent('dashboard')}>Dashboard</a> 
                </li>
                <li>
                    <a href="#" onClick={() => setActiveComponent('item')}>Items</a> 
                </li>
                <li>
                    <a href="#" onClick={() => setActiveComponent('orders')}>Orders</a> 
                </li>
                <li>
                    <a href="#" onClick={() => setActiveComponent('supplier')}>Suppliers</a>
                </li>
            </ul>
            {activeComponent === 'item' && <ItemListing isActive={true} />} 
        </div>
    );
}

export default Sidebar;

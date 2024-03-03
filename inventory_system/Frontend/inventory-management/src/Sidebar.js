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
                    <a href="#" onClick={() => setActiveComponent('dashboard')}>Dashboard</a> {/* Set active component to dashboard */}
                </li>
                <li>
                    <a href="#" onClick={() => setActiveComponent('inventory')}>Inventory</a> {/* Set active component to inventory */}
                </li>
                <li>
                    <a href="#" onClick={() => setActiveComponent('orders')}>Orders</a> {/* Set active component to orders */}
                </li>
                <li>
                    <a href="#" onClick={() => setActiveComponent('supplier')}>Suppliers</a> {/* Set active component to suppliers */}
                </li>
            </ul>
            {activeComponent === 'dashboard' && <ItemListing isActive={true} />} {/* Render ItemListing only when dashboard is active */}
        </div>
    );
}

export default Sidebar;

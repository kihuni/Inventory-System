import React, { useState } from "react";
import Header from "./Header";
import ItemListing from "./ItemListing";

const Sidebar = () => {
    const [activeComponent, setActiveComponent] = useState(<ItemListing />);

    return (
        <div className="sidebar">
            <Header />
            <ul>
                <li>
                    <a href="/dashboard">Dashboard</a>
                </li>
                <li>
                    <a href="/inventory">Inventory</a>
                </li>
                <li>
                    <a href="/orders">Orders</a>
                </li>
                <li>
                    <a href="/supplier">Suppliers</a>
                </li>
            </ul>
            {activeComponent}
        </div>
    );
}

export default Sidebar;

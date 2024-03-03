import Sidebar from './Sidebar.js';
import ItemListing from './ItemListing.js';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Sidebar /> 
        <ItemListing />
      </header>
    </div>
  );
}

export default App;

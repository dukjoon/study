import React, { useRef } from 'react';

function App() {
  const inputRef = useRef();

  return (
    <div className="App">
      <input ref={inputref} />
      <button
        onClick={() => {
          alert(inputRef.current.value);
        }}>클릭</button>
    </div>
  );
}

export default App;
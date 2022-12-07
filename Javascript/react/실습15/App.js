import React from 'react';
import Greeting from './components/Greeting';
import {useState} from 'react';
function App() {
  const [isCreated, setIsCreated] = useState(false);
  return (
    <div className="App">
      <button
        onClick={() => {
          setIsCreated(current => {
            return !current;
          });
        }}
      >
        컴포넌트 생성/제거
      </button>
      {isCreated && <Greeting />}
    </div>
  );
}

export default App;

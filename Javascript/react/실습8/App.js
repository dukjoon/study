// import React from 'react';
// import { useState } from 'react';

// function App() {
//   const [person, setPerson] = useState({
//     name: '김민수',
//     count: 0,
//   });
//   return (
//       <div className="App">
//       <button onClick = {() => {
//           setPerson((current) => {
//               current.count = current.count + 1;
//               return current;
//           })
//       }}>클릭
//       </button>
//       <span>{person.name}님이 버튼을 {person.count}회 클릭하였습니다. </span>
//       </div>
//   );

// export default App;

//잘못된 코드.
import React from 'react';
import { useState } from 'react';

function App() {
  const [person, setPerson] = useState({
    name: '김민수',
    count: 0,
  });
  return (
      <div className="App">
      <button onClick = {() => {
          setPerson((current) => {
              const newPerson = {...current};
              newPerson.count = newPerson.count + 1;
            return newPerson;
          })
      }}>클릭
      </button>
      <span>{person.name}님이 버튼을 {person.count}회 클릭하였습니다. </span>
      </div>
  )

export default App;


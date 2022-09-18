import React from 'react';
import './App.css';
import Student from './components/Student'

function App() {

    const student1 = {
        name: "김민수",
        subject: "수학",
        score: 88
    }

    const student2 = {
    name: "홍길동",
    subject: "영어",
    score: 72
}
  return (
    <div className="App">
        <Student student = {student1} />
        <Student student = {student2} />
            </div>
  );
}

export default App;

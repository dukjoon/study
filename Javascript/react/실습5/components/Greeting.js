import React from 'react';

const Greeting = props => {
  const { username } = props;
  return <h1>{ username }님 안녕하세요.</h1>;
};

export default Greeting;

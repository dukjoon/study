const name = 'elice';
const age = 5;
const nationality = 'korea';

module.exports = {
    name,
    age,
    nationality
}

const student = require('./elice');

exports.name = name;
exports.age = age;
exports.nationality = nationality;

//module을 object로 만들어서 key-value 형태로 내보낸다.



//함수형 module exports 법

// module.exports (name, age, nationality) => {
//     return {
//         name,
//         age,
//         nationality
//     }
// }
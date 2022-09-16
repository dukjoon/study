const dayjs = require("dayjs");
console.log(dayjs());

const myModule = require("./myModule");
console.log(myModule);

const myFunctionModule = require("./myFunctionModule");
console.log(myFunctionModule(age, name, nationality)); // 함수 내부의 인자를 같이 적어주어야 한다.

// myData라는 json 파일도 object로 자동 파싱되어 사용 가능하다.
const myData = require("./myData");
console.log(myData);

// module 은 cache 되기 때문에 한 가지의 모듈을 여러 번 사용하고 싶으면 함수형 모듈로 export해서 가져와야한다.

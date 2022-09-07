function fetchData() {
  return request()
    .then((response) => response.requestData)
    .catch((error) => {
      //에러 발생 코드 console.log("error!")
    });
}

//promise를 리턴하는 함수의 경우 에러가 발생하면 .catch 메서드로 이동해서 동작한다.

//catch 메서드를 사용하지 않으면 async 함수에서 try-catch 구문을 이용
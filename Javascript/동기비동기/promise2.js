promise
  .then((data) => {
    console.log("성공", data); //then 함수 실행에 성공했을 때 실행할 콜백 함수를 인자로 넘긴다.
  })
  .catch((e) => {   //catch 메서드에 실패했을 때 실행할 콜백 함수를 인자로 넘긴다.
    console.log("실패", e);
  })
  .finally(() => {  //finally 메서드는 성공 & 실패 관계 없이 실행할 콜백 함수를 인자로 넘긴다.
    console.log("promise 종료");
  });

  // then(인자1,인자2) 를 활용하면 성공시 인자1의 콜백함수, 실패시 인자2의 콜백함수 메서드를 넘길 수 있다.

  // then, catch 메서드가 또 다른 콜백 함수를 리턴해서 콜백함수에도 순서를 부여하는 것을 체인(chain) 이라고 한다.

Promise.all([promise1, promise2, promise3])

  .then((values) => {
    console.log("모두 성공:", values);
  })

  .catch((e) => {
    console.log("하나라도 실패:", e);
  });

  //promise.all 은 내부에 있는 callback 함수가 모두 실행되고 나서 처리한다.
  // 모두 성공하거나 하나라도 실패할때까지.

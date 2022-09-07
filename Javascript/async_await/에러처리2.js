async function asyncFunct() {
  try {
    let data1 = await fetchData1();
    return fetchData2(data1);
  } catch (e) {
    console.log("실패:", e);
  }
}
// catch 절의 e는 Promise의 catch 메서드가 받는 반환값과 동일하다.

// try - catch 구문을 두번 써서 세분화된 에러 처리도 가능하다.
// await 메서드는 .then 메서드의 체인처럼 순서대로 작동한다.

async function asyncFunc() {
    let data1 = await fetchData1()  // 첫번째 실행
    let data2 = await fetchData2()  // 두번째 실행
    let data3 = await fetchData3()  // 세번째 실행
    return data3
}

function promiseFunc() {
    return fetchData1()
    .then(fetchData2)
    .then(fetchData3)   //fetchData 1, 2, 3 순서대로 실행된다.
}
async function asyncFunc() {
    let data = await fetchData() // await을 붙임으로써 fetchData() .then(~~) .catch(~~) 에 있는 .then의 data가 fetchData()가 된다.
    let user = await

fetchUser(data) // fetchData, fetchUser는 Promise를 리턴하는 함수이다.
return user
}
let promise = new //new promise(callback) 함수
Promise((resolve, reject) =>  //Promise 함수는 인자로 resolve와 reject를 받는다. Promise가 성공했을 때 resolve를 호출, promise가 실패했을 때 reject를 호출
{
    if (Math.random() < 0.5) {
        return reject("실패")
    }
    resolve(10)
})
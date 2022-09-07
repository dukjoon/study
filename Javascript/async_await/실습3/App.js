import "./app.css";
import wait from "./Wait";

const App = () => {
  let cnt = 0;
  const immediateButton = document.getElementById("immediate-button");
  const afterOneSecondButton = document.getElementById(
    "after-one-second-button"
  );
  const countHeading = document.getElementById("count");

  immediateButton.addEventListener("click", () => {
    cnt += 1;
    countHeading.innerText = cnt;
  });

  afterOneSecondButton.addEventListener("click", () => {
    wait(1000).then(() => {
      cnt += 1;
      countHeading.innerText = cnt;
    });
  });

  countHeading.innerText = cnt;
};

export default App;

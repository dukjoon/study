const express = require("express");
//라우팅
const router = express.Router();
router.get('/', (req,res,next) => {
    res.send('respond with a resource')
})

module.export = router;

const app = express();
app.get("/", (req, res) => {
  res.send("hello express");
});

app.listen(3000, () => {
  console.log("Server Started");
});

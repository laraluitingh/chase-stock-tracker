const searchField = document.getElementById("searchField");
const dropdown = document.getElementById("dropdown");
const errorMessage = document.getElementById("notExist");
const searchBody = document.getElementById("search-body");
const searchBox = document.getElementById("search-box");
// function checkIfStockExists(sybmol, callback) {
// call the call back function when when i have the data
// data = axios
//   .get(`http://127.0.0.1:3000/check_stock/${sybmol}`)
//   .then((response) => {
// console.log(response.data+ " " + typeof response.data)
//       callback(response.data);
//     })
// }
function checkIfStockExists(symbol, list, object) {
  // call the call back function when when i have the data
  axios
    .get(`/check_stock/${symbol}`)
    .then((response) => {

      return response.data;
    })
    .then((data) => {
      console.log(data)
      if (data) {
        console.log(Object.values(object)[0]);
        let li = document.createElement("li");
        let spanSymbol = document.createElement("span");
        spanSymbol.textContent = Object.values(object)[0];
        spanSymbol.classList.add("symbol-dropdown");
        let spanName = document.createElement("span");
        spanName.textContent = Object.values(object)[1];
        spanSymbol.classList.add("name-dropdown");
        li.setAttribute("data-title", Object.values(object)[0]);
        li.setAttribute("class", "dropdown-list-item");
        // li.textContent = Object.values(element)[0];
        li.addEventListener("click", () => {
          dropdown.innerHTML = "";
          searchField.value = li.getAttribute("data-title");
        });
        list.appendChild(li);
        li.append(spanSymbol);
        li.append(spanName);
      }
    });
}

function getStocks(searchTerm) {
  axios
    .get(
      `https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${searchTerm}&apikey=0HB84RQA74HAVDLB`
    )
    .then((response) => {
      // console.log(response.data)
      dropdown.innerHTML = "";
      if ("bestMatches" in response.data) {
        array = response.data.bestMatches;
        const list = document.createElement("ul");
        list.setAttribute("class", "dropdown-list");
        dropdown.append(list);
        for (let i = 0; i < array.length; i++) {
          object = array[i];
    
          checkIfStockExists(Object.values(object)[0], list, object);
        }
      }
    });
}
searchField.addEventListener("input", () => {
  console.log("click!");
  const symbolSearch = searchField.value;
  console.log(symbolSearch);
  getStocks(symbolSearch);
});
function DisplayErrorMessage() {
  if (errorMessage) {
    const divError = document.getElementById("for-error-message");
    console.log("no stock exists");
    const div = document.createElement("div");
    div.id = "error-message";
    div.textContent = errorMessage.value;
    div.classList.add("incorrect-singup");
    divError.appendChild(div);
  }
}
DisplayErrorMessage();
function RemoveErrorMessage() {
  const error = document.getElementById("error-message");
  if (error) {
    error.remove();
  }
}
setTimeout(RemoveErrorMessage, 5000);

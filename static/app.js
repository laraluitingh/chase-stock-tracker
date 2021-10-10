const searchField = document.getElementById("searchField");
const dropdown = document.getElementById("dropdown");
const errorMessage = document.getElementById("notExist");
const searchBody = document.getElementById("search-body");
const searchBox = document.getElementById("search-box");

function checkIfStockExists(sybmol) {
  data = axios
    .get(`http://127.0.0.1:3000/check_stock/${sybmol}`)
    .then((response) => {
      console.log(response.data+ " " + typeof response.data)
      return response.data;
    })
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
          element = array[i];
          // response = checkIfStockExists(Object.values(element)[0]);
          if (Object.values(element)[3]== "United States") {
            console.log(Object.values(element)[0]);
            let li = document.createElement("li");
            let spanSymbol =document.createElement("span")
            spanSymbol.textContent= Object.values(element)[0];
            spanSymbol.classList.add("symbol-dropdown")
            let spanName =document.createElement("span")
            spanName.textContent= Object.values(element)[1]
            spanSymbol.classList.add("name-dropdown")
            li.setAttribute("data-title", Object.values(element)[0]);
            li.setAttribute("class", "dropdown-list-item");
            // li.textContent = Object.values(element)[0];
            li.addEventListener("click", () => {
              dropdown.innerHTML = "";
              searchField.value = li.getAttribute("data-title");
            });
            list.appendChild(li);
            li.append(spanSymbol)
            li.append(spanName)
          } else {
            continue;
          }
        }
      }
    });
}

searchField.addEventListener("input", () => {
  console.log("click!");
  const symbolSearch = searchField.value;
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

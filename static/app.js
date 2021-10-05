const searchField = document.getElementById("searchField");
const dropdown = document.getElementById("dropdown");

function getStocks(searchTerm) {
  axios
    .get(
      `https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${searchTerm}&apikey=0HB84RQA74HAVDLB`
    )
    .then((response) => {
      // console.log(response.data)
      dropdown.innerHTML = "";
      array = response.data.bestMatches;
      const list = document.createElement("ul");
      list.setAttribute("class", "dropdown-list");
      dropdown.append(list);
      for (let i = 0; i < array.length; i++) {
        element = array[i];
        if (Object.values(element)[3] === "United States") {
          console.log(Object.values(element)[0]);
          let li = document.createElement("li");
          li.setAttribute("data-title", Object.values(element)[0]);
          li.setAttribute("class", "dropdown-list-item");
          li.textContent = Object.values(element)[0];
          li.addEventListener("click", () => {
            dropdown.innerHTML = "";
            searchField.value = li.getAttribute("data-title");
          });
          list.appendChild(li);
        }else{
            continue;
        }
      }
    });
}

searchField.addEventListener("input", () => {
  console.log("click!");
  const symbolSearch = searchField.value;
  getStocks(symbolSearch);
});

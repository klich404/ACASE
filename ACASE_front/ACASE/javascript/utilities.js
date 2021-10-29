// Function to return keywords values to button "Palabras claves"
function getFetchKeywords () {
  (async () => {
    const keywords = await axios.get('http://127.0.0.1:8000/keywords/');
    let listKeywords = ``
    keywords.data.forEach(element => {
      listKeywords += `<option id="keywords-tag" value=${element.Word}></option>`
    })
    const datalist = document.getElementById('keywords')
    datalist.innerHTML = listKeywords;
  })();
}

// Function to return url values to button "URL"
function getFetchUrl () {
  (async () => {
    const url = await axios.get('http://127.0.0.1:8000/target/');
    let urlList = ``
    url.data.forEach(element => {
      urlList += `<option value=${element.Name}></option>`
    });
    const listUrl = document.getElementById('url-list')
    listUrl.innerHTML = urlList;
  })();
}

export { getFetchKeywords, getFetchUrl };

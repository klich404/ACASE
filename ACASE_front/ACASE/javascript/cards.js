class Inbox {
  // Get API information
  getFetchApi () {
    (async () => { 
      try {
        const response = await axios.get('http://127.0.0.1:5000/card');
        const keywords = await axios.get('http://127.0.0.1:5000/keywords');
        const url = await axios.get('http://127.0.0.1:5000/url');
        this.keywordsList(keywords.data);
        this.makeCards(response.data);
        this.urlGet(url.data);
      } catch(error) {
        console.log(error);
      }
      })();
    }
    // Function to send the keywords list to HTML tag
    keywordsList(keywords) {
      let listKeywords = ``
      keywords.forEach(element => {
        listKeywords += `<option value=${element}></option>`
      })
      const datalist = document.getElementById('keywords')
      datalist.innerHTML = listKeywords;
    }
    // Function to get elements from url 
    urlGet(url) {
      let urlList = ``
      url.forEach(element => {
        urlList += `<option value=${element}></option>`
      });
      const listUrl = document.getElementById('url')
      listUrl.innerHTML = urlList;
    }
    // Function to create the HTML of cards 
    makeCards (cards) {
      let htmlElements = ``
      cards.forEach(element => {
        htmlElements += `<div class="col-lg-4 p-3">
          <div class="card">
          <div class="card-body p-2">
            <h5 class="card-title mb-1">${element.title}</h5>
            <p class="card-text mb-2"> ${element.text}
            </p>
            <p class="date mb-1"><b>Fecha: </b>${element.date}</p>
            <p class="source-url mb-2"><b>Fuente:</b> ${element.url}/</p>
          </div>
        </div>
        <div class="cards-buttons">
            <a href="${element.url}" target="_blank" class="btn btn-primary">Visitar</a>
            <img id="drop-button" class="trash-icon" src="./icons/trash.png" alt="trash">
            <img id="select-button" class="check-icon" src="./icons/check-file.png" alt="check">
        </div>
        </div>`
      });
      const cardsContainer = document.getElementById('cards-container');
      cardsContainer.innerHTML = htmlElements;
    }
}

export { Inbox }

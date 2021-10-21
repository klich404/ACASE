class Inbox {
  // Get API information
  getFetchApi(keyWord = null) {
    (async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/card');
        let responseList = response.data; // All objects 10 []
        if (keyWord) responseList = this.filterKeyword(keyWord, responseList); // Filter object 1 []
        this.makeCards(responseList); // 10 [] o 1 [] depeding if keyword exists
      } catch (error) {
        console.log(error);
      }
    })(); 
  };

  // Function return the cards to final user
  makeCards(cards) {
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
            <a href="${element.url}" target="_blank" class="btn btn-primary">Visitar</a>
            <a href="#" target="_blank" class="btn btn-primary">Modificar</a>
            <img id="drop-button" class="trash-icon" src="./icons/trash.png" alt="trash">
            <img id="select-button" class="check-icon" src="./icons/check-file.png" alt="check">
          </div>
          </div>
        </div>`
    });
    const cardsContainer = document.getElementById('cards-container');
    cardsContainer.innerHTML = htmlElements;
  }
  filterKeyword(keyWord, response) {
    let listObject = []
    response.forEach(element => {
      if (element.Associated_KW === keyWord) {
        listObject.push(element)
      }
    })
    return listObject;
  }
}

export { Inbox }
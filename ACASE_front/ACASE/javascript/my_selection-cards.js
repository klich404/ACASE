class mySelectionCards {
  getElementsToMyList () {
    (async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/card/');
        let entireList = response.data; // All objects 10 []
        let responseList = []
        entireList.forEach(e => {
          if (e.My_selection == true && e.Trash_section == false)
            responseList.push(e)
        })
         let cards = this.makeCards(responseList);
        document.getElementById('cards-container').innerHTML = cards;
        /*this.showForm();
        this.toMySelection();
        this.toTrash();*/
      } catch (error) {
        console.log(error);
      }
    })();
  }
  makeCards(cards) {
    let htmlElements = ``
    cards.forEach(element => {
      htmlElements += `<div id="${element.Id}" class="col">
      <div class="card m-2">
      <div class="card-body">
      <div>
      <h3 class="card-title mb-1">${this.truncateTitle(element.Title)}</h3>
      <p class="card-text mb-2"> ${this.truncateText(element.Text)}
      </p>
      </div>
      <div>
      <p class="date mb-1"><b>Fecha: </b>${element.Date}</p>
      <p class="source-url mb-2"><b>Fuente:</b> ${this.truncateUrl(element.Url)}/</p>
      </div>
      <div>
      <a href="${element.Url}" target="_blank" class="btn btn-primary">Visitar</a>
      <a data-id="${element.Id}" href="#" class="modify-button btn btn-primary">Modificar</a>
      <img id="${element.Id}" class="trash-icon" src="./icons/times-circle-regular.svg" alt="trash">
      </div>
      </div>
      </div>
      </div>`
    });
    return htmlElements
  }
// Truncate the text with 180 words 
  // Truncate Title
  truncateTitle(text, limit = 90) {
    return (text.length <= limit)
      ? text
      : text.slice(0, limit) + "..."
  }
  // Truncate the text with 180 words 
  truncateText(text, limit = 180) {
    return (text.length <= limit)
      ? text
      : text.slice(0, limit) + "..."
  }
  // Truncate the text with 180 words 
  truncateUrl(text, limit = 90) {
    return (text.length <= limit)
      ? text
      : text.slice(0, limit) + "..."
  }

}

export { mySelectionCards }

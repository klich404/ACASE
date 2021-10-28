class trashCards {
  getElementsToTrash() {
    (async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/card/');
        let entireList = response.data; // All objects 10 []
        let responseList = []
        entireList.forEach(e => {
          if (e.My_selection == false && e.Trash_section == true)
          responseList.push(e)
        })
        console.log(responseList);
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
      htmlElements += `<div id="${element.Id}" class="col-lg-4 p-3">
      <div class="card">
      <div class="card-body p-2">
      <div>
      <h5 class="card-title mb-1">${element.Title}</h5>
      <p class="card-text mb-2"> ${this.truncateText(element.Text)}
      </p>
      <p class="date mb-1"><b>Fecha: </b>${element.Date}</p>
      <p class="source-url mb-2"><b>Fuente:</b> ${element.Url}/</p>
      </div>
      <div>
      <a href="${element.Url}" target="_blank" class="btn btn-primary">Visitar</a>
      <a data-id="${element.Id}" href="#" class="modify-button btn btn-primary">Modificar</a>
      <img id="${element.Id}" class="trash-icon" src="./icons/delete_file.png" alt="trash">
      <img id="${element.Id}" class="check-icon" src="./icons/save_file.png" alt="check">
      </div>
      </div>
      </div>
      </div>`
    });
    return htmlElements
  }
  // Truncate the text with 180 words 
  truncateText(text, limit = 180) {
    return (text.length <= limit)
      ? text
      : text.slice(0, limit) + "..."
  }

}

export { trashCards }

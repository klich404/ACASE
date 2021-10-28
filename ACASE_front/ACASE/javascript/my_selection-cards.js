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
      htmlElements += `<div id="${element.id}" class="col-lg-4 p-3">
      <div class="card">
      <div class="card-body p-2">
      <div>
      <h5 class="card-title mb-1">${element.title}</h5>
      <p class="card-text mb-2"> ${this.truncateText(element.text)}
      </p>
      <p class="date mb-1"><b>Fecha: </b>${element.date}</p>
      <p class="source-url mb-2"><b>Fuente:</b> ${element.url}/</p>
      </div>
      <div>
      <a href="${element.url}" target="_blank" class="btn btn-primary">Visitar</a>
      <a data-id="${element.id}" href="#" class="modify-button btn btn-primary">Modificar</a>
      <img id="${element.id}" class="trash-icon" src="./icons/delete_file.png" alt="trash">
      <img id="${element.id}" class="check-icon" src="./icons/save_file.png" alt="check">
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

export { mySelectionCards }

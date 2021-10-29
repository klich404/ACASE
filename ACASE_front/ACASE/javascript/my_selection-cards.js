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
        this.showModifiedData(responseList);
        /*this.toMySelection();
        this.toTrash();*/
      } catch (error) {
        console.log(error);
      }
    })();
}
  makeCards(cards) {
    let htmlElements = ``
    cards.forEach(element => {
      htmlElements += `<div id="${element.id}" class="col">
      <div class="card mb-2">
      <div class="card-body">
      <div>
      <h3 class="card-title mb-3">${this.truncateTitle(element.Title)}</h3>
      <p class="card-text mb-2"> ${this.truncateText(element.Text)}</p>
      </div>
      <div>
      <p class="date mb-1"><b>Fecha: </b>${element.Date}</p>
      <p class="source-url"><b>Fuente:</b> ${this.truncateUrl(element.Url)}/</p>
      <a href="${element.Url}" target="_blank" class="btn btn-primary">Visitar</a>
      <a data-id="${element.id}" href="#" class="modify-button btn btn-primary">Modificar</a>
      <img id="${element.id}" class="trash-icon" src="./icons/times-circle-regular.svg" alt="trash">
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

// Filtering the modified data from object
  showModifiedData(data) {
    let AllData = []
    data.forEach(dataElements => {
      AllData.push({id: dataElements.id, title: dataElements.Title, relevance: dataElements.Relevance, learning: dataElements.Learning, finding: dataElements.Finding, pages: dataElements.Pages})
    })
    this.filteringData(AllData)
    return AllData
  }

  filteringData (data) {
   data.forEach(element => {
      document.querySelectorAll(".modify-button").forEach(e => {
        e.addEventListener('click', () => {
          if (e.getAttribute('data-id') === element) {
            console.log(element[element.id])
          }
        })
      })
    })
  }

}
export { mySelectionCards }

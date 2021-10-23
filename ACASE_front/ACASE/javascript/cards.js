class Inbox {
  // Get API information
  getFetchApi(keyWord = null, urlValue = null) {
    (async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/card/');
        let responseList = response.data; // All objects 10 []
        if (keyWord) responseList = this.filterKeyword(keyWord, responseList); // Filter object 1 []
        let cards = this.makeCards(responseList); // 10 [] o 1 [] depeding if keyword exists
        document.getElementById('cards-container').innerHTML = cards;
        this.showForm();
        //this.filterUrl(urlValue, responseList);
      } catch (error) {
        console.log(error);
      }
    })();
  };

  // This function create the tags and give the respective values
  makeCards(cards) {
    let htmlElements = ``
    cards.forEach(element => {
      htmlElements += `<div id="1175171e-0950-43e2-a881-72ca165c890d-${element.id}" class="col-lg-4 p-3">
          <div class="card">
          <div class="card-body p-2">
            <h5 class="card-title mb-1">${element.title}</h5>
            <p class="card-text mb-2"> ${element.text}
            </p>
            <p class="date mb-1"><b>Fecha: </b>${element.date}</p>
            <p class="source-url mb-2"><b>Fuente:</b> ${element.url}/</p>
            <a href="${element.url}" target="_blank" class="btn btn-primary">Visitar</a>
            <a data-id="1175171e-0950-43e2-a881-72ca165c890d-${element.id}" href="#" class="modify-button btn btn-primary">Modificar</a>
            <img id="drop-button" class="trash-icon" src="./icons/trash.png" alt="trash">
            <img id="select-button" class="check-icon" src="./icons/check-file.png" alt="check">
          </div>
          </div>
        </div>`
    });
    return htmlElements
  }

// This function works with the button "Palabra clave" filtering the cards with
  filterKeyword(keyWord, response) {
    let listObject = []
    response.forEach(element => {
      if (element.Associated_KW === keyWord) {
        listObject.push(element)
      }
    })
    return listObject;
  }

/*   filterUrl(url, response) {
    response.forEach(element => {
      console.log(element.url);
    }) 
   }*/

// Function to listen click of Button "Modificar" and open the form with the method createOverlay
  showForm () {
    document.querySelectorAll('.modify-button').forEach(e => {
      e.addEventListener('click', () => {
        let form = this.createOverlay(e.getAttribute('data-id'));
        let body = document.querySelector('body')
        let parentElement = document.createElement('div');
        parentElement.setAttribute('id', 'div-form');
        parentElement.innerHTML = form
        body.appendChild(parentElement)
        this.closeForm(parentElement.getAttribute('id'));
      })
    })
  }

// Function to close the form after click
  closeForm(dataId) {
    document.getElementById('close-form').addEventListener('click', () => {
      document.getElementById(dataId).remove();
    });
  }

// Function to create the html content after click in button "Modificar"
      createOverlay(dataId) {
        let title = document.getElementById(dataId).querySelector('h5').innerText;
        return `  <div class="container-fluid prompt-overlay">
    <div class="prompt">
      <h2>${title}</h2>
      <h3> </h3>
      <form>
        <div class="form-control">
          <label for="relevant-message">¿Por qué es relevante este artículo?</label>
          <textarea id="relevant-message" cols="60" rows="2" placeholder="Ingresa el texto" name="relevant_message" class="input-field"
            ></textarea>
        </div>
        <div class="form-control">
          <label for="relevant-learning">¿Qué vas a aprender de este artículo?</label>
          <textarea id="relevant-learning" cols="60" rows="2" placeholder="Ingresa el texto" name="relevant_learning" class="input-field"
            ></textarea>
        </div>
        <div class="form-control">
          <label for="relevant-encounter">¿Cuál es el hallazgo más importante que vas a encontrar aquí?</label>
          <textarea id="relevant-encounter" cols="60" rows="2" placeholder="Ingresa el texto" name="relevant_encounter" class="input-field"
            ></textarea>
        </div>
        <div class="form-control">
          <label for="pages">Página de inicio y final</label>
          <textarea id="pages" cols="60" rows="2" placeholder="Ingresa el texto" name="pages" class="input-field"
            ></textarea>
        </div>
        <button id="close-form">Cerrar</button>
        <input type="submit" value="Enviar" id="submit-btn" class="submit-btn">
      </form>
    </div>
  </div>`
      }
}

export { Inbox }
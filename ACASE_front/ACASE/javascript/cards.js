class Inbox {
// Get API information
  getFetchApi(keyWord = null, urlValue = null) {
    (async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/card/');
        let responseList = response.data; // All objects 10 []
        //let = responseList = []
/*         entireList.forEach(e => {
        if (e.My_selection == false && e.Trash_section == false)
          responseList.push(e)
        }) */
        // It works if with Palabra clave match with keywords
        if (keyWord) {
          responseList = this.filterKeyword(keyWord, responseList); // Filter object 1 []
          let cards = this.makeCards(responseList); // 10 [] o 1 [] depeding if keyword exists
          document.getElementById('cards-container').innerHTML = cards;
        // It work if with Pagina Web matchs with url
        } if (urlValue) {
          responseList = this.filterUrl(urlValue, responseList);
          let cards = this.makeCards(responseList);
          document.getElementById('cards-container').innerHTML = cards;
        // It works with Palabra clave and Pagina Web
        } if (keyWord && url) {
          responseList = this.filterKeyAndValue(keyWord, url, responseList);
          let cards = this.makeCards(responseList);
          document.getElementById('cards-container').innerHTML = cards;
        // It works if there's not any match
        } else {
          let cards = this.makeCards(responseList);
          document.getElementById('cards-container').innerHTML = cards;
        }
      this.showForm();
      this.toMySelection();
      } catch (error) {
        console.log(error);
      }
    })();
  };
// This function create the tags and give the respective values
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
  truncateText (text, limit = 180) {
    return (text.length <= limit)
      ? text
      : text.slice(0, limit) + "..."
  }
  toMySelection () {
    document.querySelectorAll('.check-icon').forEach(e => {
      e.addEventListener('click', () => {
        let paidLoad = {}
        paidLoad['id'] = e.getAttribute('id')
        paidLoad['My_selection'] = true;
        (async () => {
          try { 
            const response = await axios.post('http://127.0.0.1:8000/my_selection/', {
              id:  e.getAttribute('id'),
              My_selection: true
            })
          } catch (error) {
            console.error(error);
          }
          alert('Tu carta se ha enviado a Selección')
          document.getElementById(e.getAttribute('id')).remove()
        })();
      })
  })
}
// This function works with the button "Palabra clave" filtering the cards with
  filterKeyword(keyWord, response) {
    let listObjectbyKey = []
    response.forEach(element => {
      if (element.Associated_KW === keyWord) {
        listObjectbyKey.push(element)
      }
    })
    return listObjectbyKey;
  }
// This function return the url list matched with the button Pagina web
      filterUrl(url, response) {
        let listObjectByUrl = []
      response.forEach(element => {
        if (element.source_url === url)
          listObjectByUrl.push(element)
      })
        return listObjectByUrl;
     }
// This function return all the element matched with Palabra Clave and Pagina Web
  filterKeyAndValue(keyWord, url, response) {
    let listObjectKeyAndValue = []
    response.forEach(element => {
      if (element.source_url === url && element.Associated_KW === keyWord)
      listObjectKeyAndValue.push(element);
    })
    return listObjectKeyAndValue;
  }

// Function to create the html content after click in button "Modificar"
    createOverlay(dataId) {
      let title = document.getElementById(dataId).querySelector('h5').innerText;
      let formPage =  `<div class="container-fluid vh-100 prompt-overlay">
        <div class="prompt">
          <h2 class="title-text-form">${title}</h2>
          <form action="http://127.0.0.1:8000/form/" method="POST">
            <div class="form-control">
              <label class="form-questions" for="relevance">¿Por qué es relevante este artículo?</label>
              <textarea id="relevance" cols="60" rows="2" placeholder="Ingresa tu texto" name="relevance"
                class="input-field"></textarea>
            </div>
            <div class="form-control">
              <label class="form-questions" for="learning">¿Qué vas a aprender de este artículo?</label>
              <textarea id="learning" cols="60" rows="2" placeholder="Ingresa tu texto" name="learning"
                class="input-field"></textarea>
            </div>
            <div class="form-control">
              <label class="form-questions" for="finding">¿Cuál es el hallazgo más importante que vas a
                encontrar aquí?</label>
              <textarea id="finding" cols="60" rows="2" placeholder="Ingresa tu texto"
                name="finding" class="input-field"></textarea>
            </div>
            <div class="form-control">
              <label class="form-questions" for="page">Página de inicio y final</label>
              <textarea id="page" cols="60" rows="2" placeholder="Ingresa tu texto" name="page"
                class="input-field"></textarea>
            </div>
            <button id="close-form">Cerrar</button>
            <input type="hidden" value="${dataId}" name="id">
            <input type="submit" value="Enviar" id="submit-btn" class="submit-btn">
          </form>
        </div>
      </div>`
      console.log(formPage)
      return formPage
    }
// Function to listen click of Button "Modificar" and open the form with the method createOverlay
  showForm() {
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
}

export { Inbox }
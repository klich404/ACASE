import { Inbox } from './cards.js';
const searchButton = document.getElementById('search-button');

window.addEventListener('load', function () {
  const newObject = new Inbox();
  searchButton.addEventListener('click', () => newObject.getFetchApi());
  const keywords = new Inbox();
  keywords.getFetchApi();
  const url = new Inbox();
  url.getFetchApi();
});

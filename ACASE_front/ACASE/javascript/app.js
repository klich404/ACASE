import { Inbox } from './cards.js';
import { getFetchKeywords, getFetchUrl } from './utilities.js';
const searchButton = document.getElementById('search-button');

window.addEventListener('load', function () {
  getFetchKeywords();
  getFetchUrl();
  //searchButton.addEventListener('click', () => newObject.getFetchApi());
  searchButton.addEventListener('click', () => {
    const KeyWord = document.getElementById('keywords-list');
    const newObject = new Inbox();
    newObject.getFetchApi(KeyWord.value);
  });
});

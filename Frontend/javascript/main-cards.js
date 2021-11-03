import { Inbox } from './cards.js';
import { getFetchKeywords, getFetchUrl } from './utilities.js';
const searchButton = document.getElementById('search-button');

window.addEventListener('load', function () {
  /*This is the logic of Bandeja Principal */
  //Function to get Keywords in output
  getFetchKeywords();
  // Function to get URL in output
  getFetchUrl();
  // Button to filter result from DB
  searchButton.addEventListener('click', () => {
    const KeyWordValue = document.getElementById('keywords-input');
    const urlValue = document.getElementById('url-input');
    const newObject = new Inbox();
    newObject.getFetchApi(KeyWordValue.value, urlValue.value);
  });
});
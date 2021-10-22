import { Inbox } from './cards.js';
import { getFetchKeywords, getFetchUrl } from './utilities.js';
const searchButton = document.getElementById('search-button');

window.addEventListener('load', function () {
  //Function to get Keywords in output
  getFetchKeywords();
  // Function to fet URL in output
  getFetchUrl();
  // Button to filter result from DB
  searchButton.addEventListener('click', () => {
    const KeyWordValue = document.getElementById('keywords-input');
    const urlValue = document.getElementById('url-input');
    const newObject = new Inbox();
    newObject.getFetchApi(KeyWordValue.value, urlValue.value);
  });
});

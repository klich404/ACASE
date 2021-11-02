import { trashCards } from './trash-cards.js'
let trashButton = document.getElementById('trash-button');

window.addEventListener('load', function () {
  /* This is the logic of Papelera */
  let selectionObject = new trashCards();
  selectionObject.getElementsToTrash();
});

import { mySelectionCards } from './my_selection-cards.js'

window.addEventListener('load', function () {
  /* This is the logic of Selección */
    let selectionObject = new mySelectionCards();
    selectionObject.getElementsToMyList();
});
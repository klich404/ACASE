var imageSources = ["./img/slight-2.png", "./img/slight-1.png", "./img/slight-3.png", "./img/slight-4.png", "./img/slight-5.png"]

var index = 0;
setInterval(function () {
  if (index === imageSources.length) {
    index = 0;
  }
  document.getElementById('image').src = imageSources[index];
  index++;
}, 3000);

var imagesAcase = ["./img/with-information.png", "./img/without-information.png"]

var index = 0;
setIntervalTwo(function () {
  if (index === imagesAcase.length) {
    index = 0;
  }
  document.getElementById('slight-acase').src = imagesAcase[index];
  index++;
}, 3000);

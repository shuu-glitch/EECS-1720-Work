alert('They are watching you now! Tread carefully. :)');

let filenames = [
  'eye1.png',
  'eye2.png',
  'eye3.png',
  'eye4.png',
  'eye5.png',
  'eye6.png',
  'eye7.png',
  'eye8.png'
];

let imgs = document.getElementsByTagName('img');

for (let imgElt of imgs) {
  let r = Math.floor(Math.random() * filenames.length);
  let file = 'images/' + filenames[r];
  let url = chrome.extension.getURL(file);
  imgElt.src = url;
  console.log(url);
}

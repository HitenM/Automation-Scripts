// Function to recursively traverse the DOM tree and translate all text nodes
function translateNode(node) {
  if (node.nodeType === Node.TEXT_NODE) {
    // Translate the text content of the node
    const text = node.textContent.trim();
    if (text.length > 0) {
      // Send the text to Google Translate API and replace the node's text content with the translation
      fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=hi&dt=t&q=${encodeURIComponent(text)}`)
        .then(response => response.json())
        .then(data => {
          const translation = data[0][0][0];
          node.textContent = translation;
        })
        .catch(error => console.error(error));
    }
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    // Recursively translate the child nodes of the element
    for (const childNode of node.childNodes) {
      translateNode(childNode);
    }
  }
}

// Translate all text nodes on the page
const textNodes = document.querySelectorAll('*:not(script):not(style)');
for (const node of textNodes) {
  translateNode(node);
}

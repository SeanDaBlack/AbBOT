/* globals chrome */
(({ assign }) => (
  document.querySelector('head').appendChild(
    assign(document.createElement('script'), {
      type: 'module',
      src: chrome.runtime.getURL('./src/index.js'),
    }),
  )
))(Object);

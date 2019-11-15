/*
 * Main Javascript file.
 *
 * This file bundles all of your javascript together using webpack.
 */

// Support Content Security Policy = script-src: 'nonce-<random-value>'
// eslint-disable-next-line no-undef
__webpack_nonce__ = window.NONCE;

// Check if Dynamic import() is supported by the browser
function supportsDynamicImport() {
  try {
    import('./module/empty.js');
    return true;
  } catch {
    return false;
  }
}

// If dynamic import is not supported, redirect.
const redirectTo = '/not-supported';
const currentUrl = window.location.pathname;

if (currentUrl !== redirectTo) {
  if (!supportsDynamicImport()) {
    window.location.replace(redirectTo);
  }
}

/*
Where dynamic import starts
Usage:
    - In your <script id="main_js"> tag, add 'data-view' attribute and assign the module you want to be loaded
*/

const view = document.getElementById('main_js').getAttribute('data-view');
const dataRoutes = [`${view}`];

const loadModules = (modules) => Promise.all(
    modules.map((module) => import(`./view/${module}.js`)
        .then((obj) => {
          obj.default();
        })
        .catch(() => {}),),
  );

loadModules(dataRoutes);

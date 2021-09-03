import randomText from './randomText.js';
import randomZip from './randomZip.js';
import randomName from './randomName.js';

const { city, zip, county } = randomZip();

const delay = t => new Promise(r => setTimeout(r, t));

const selector = async (sel, time = 20000, poll = 100) => {
  const start = Date.now();
  while (!document.querySelector(sel) && Date.now() - start < time) {
    await delay(poll);
  }
  const result = document.querySelector(sel);
  if (!result) {
    throw new Error(`Timed out waiting for ${sel} on page`);
  }
  return result;
};

const typeText = async (sel, text) => {
  const field = (await selector(sel));
  field.value = text;
  await delay(100);
  let event = document.createEvent('HTMLEvents');
  event.initEvent('keyup', false, true);
  field.dispatchEvent(event);
  await delay(100);
  event = document.createEvent('HTMLEvents');
  event.initEvent('change', false, true);
  field.dispatchEvent(event);
  return field;
};

const notify = async () => {
  if (await Notification.requestPermission() === 'granted') {
    const notification = new Notification(
      'A new reCAPTCHA is ready',
      {  },
    );
    notification.onclick = () => {
      window.focus();
      return false;
    };
  }
};

(async () => {
  try {
    await typeText('form textarea[name="textarea-1"]', randomText(5000, 450));
    await typeText('form input[name="text-1"]', randomText(2000, 140));
    await typeText('form input[name="text-6"]', randomName());
    await typeText('form input[name="text-2"]', city);
    await typeText('form input[name="text-3"]', "TX");
    await typeText('form input[name="text-4"]', zip);
    await typeText('form input[name="text-5"]', county);
    (await selector('form input[value="no"]+.forminator-checkbox-box')).click();
    (await selector('form')).addEventListener('submit', async () => {
      await delay(5000);
      window.location.reload();
    });
    if (!document.querySelector('iframe[title="reCAPTCHA"]')) {
      (await selector('form')).submit();
    } else {
      await notify();
    }
  } catch (e) {
    // Form probably didn't load; refresh the page
    window.location.reload();
  }
})();

/* eslint-env browser */
(() => {
  let applicationServerKey = "";
  let projectId = "";
  let serviceWorkerUrl = "/sw.js";
  const API_URL = "https://api.webpush.cc";
  const getLang = () =>
    navigator.language || navigator.browserLanguage || (navigator.languages || ["ru"])[0];
  const hexToArrayBuffer = (hex) => {
    const strBytes = hex.match(/.{2}/g);
    const bytes = new Uint8Array(strBytes.length);
    for (let i = 0; i < strBytes.length; i += 1) {
      bytes[i] = parseInt(strBytes[i], 16);
    }
    return bytes;
  };
  const postToServer = async (url, data) => {
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone || null;
    const locale = getLang();
    return fetch(API_URL + url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...data, timezone, locale }),
    });
  };
  const registerServiceWorker = () => {
    if (serviceWorkerUrl === null) {
      return;
    }

    if (!("serviceWorker" in navigator)) {
      console.log("This browser doesn't support service workers.");
      return;
    }
    navigator.serviceWorker
      .getRegistration()
      .then((registration) => {
        if (registration) {
          console.log(`Service worker registered. Scope: ${registration.scope}`);
          return;
        }
        navigator.serviceWorker
          .register(serviceWorkerUrl, { updateViaCache: "none" })
          .then(() => {
            console.log(`Service worker registered.`);
          })
          .catch((error) => console.error(error));
      })
      .catch((error) => console.error(error));
  };

  const init = async (id, swDisable = false) => {
    if (swDisable) {
      serviceWorkerUrl = null;
    }
    projectId = id;

    registerServiceWorker();

    return new Promise((resolve, reject) => {
      postToServer("/init", { projectId })
        .then((response) => response.json())
        .then((data) => {
          if (!data.status) {
            reject(new Error("INIT_ERROR"));
            return;
          }
          applicationServerKey = hexToArrayBuffer(data.applicationServerKey);
          resolve({ status: "INIT" });
        })
        .catch((error) => reject(error));
    });
  };

  const subscribe = async () => {
    return new Promise((resolve, reject) => {
      if (!applicationServerKey) {
        reject(new Error("APPLICATION_KEY_NOT_SET"));
        return;
      }
      navigator.serviceWorker
        .getRegistration()
        .then((registration) => {
          registration.pushManager.getSubscription().then((subscription) => {
            if (subscription) {
              resolve({ status: "ALREADY_SUBSCRIBED" });
              return;
            }

            registration.pushManager
              .subscribe({
                userVisibleOnly: true,
                applicationServerKey,
              })
              .then((newSubscription) => {
                if (!newSubscription) {
                  reject(new Error("SUBSCRIBE_ERROR"));
                  return;
                }
                const { endpoint, keys } = newSubscription.toJSON();

                postToServer("/subscription/add", { projectId, endpoint, keys })
                  .then((response) => response.json())
                  .then((data) => {
                    if (!data.status) {
                      reject(new Error("SUBSCRIBE_ERROR"));
                      return;
                    }
                    resolve({ status: "SUBSCRIBE", clientId: data.clientId });
                  })
                  .catch((error) => reject(error));
              });
          });
        })
        .catch((error) => reject(error));
    });
  };

  const unsubscribe = async () => {
    return new Promise((resolve, reject) => {
      navigator.serviceWorker
        .getRegistration()
        .then((registration) => {
          registration.pushManager.getSubscription().then((subscription) => {
            if (!subscription) {
              reject(new Error("ACTIVE_SUBSCRIBE_NOT_FOUND"));
              return;
            }
            postToServer("/subscription/remove", {
              endpoint: subscription.endpoint,
            })
              .then(() => {
                subscription.unsubscribe();
                resolve({ status: "UNSUBSCRIBE" });
              })
              .catch((error) => reject(error));
          });
        })
        .catch((error) => reject(error));
    });
  };
  const isPushNotificationSupported = async () => {
    return "PushManager" in window;
  };

  window.WebPush = {
    init,
    subscribe,
    unsubscribe,
    isPushNotificationSupported,
  };
})();

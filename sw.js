const CACHE_NAME = 'snake-game-v1.0.0';
const urlsToCache = [
  '/tanchishe/snake_mobile_wechat_fullscreen_pwa.html',
  '/tanchishe/manifest.json',
  '/tanchishe/icons/icon-16x16.png',
  '/tanchishe/icons/icon-32x32.png',
  '/tanchishe/icons/icon-48x48.png',
  '/tanchishe/icons/icon-72x72.png',
  '/tanchishe/icons/icon-96x96.png',
  '/tanchishe/icons/icon-128x128.png',
  '/tanchishe/icons/icon-144x144.png',
  '/tanchishe/icons/icon-152x152.png',
  '/tanchishe/icons/icon-167x167.png',
  '/tanchishe/icons/icon-180x180.png',
  '/tanchishe/icons/icon-192x192.png',
  '/tanchishe/icons/icon-256x256.png',
  '/tanchishe/icons/icon-384x384.png',
  '/tanchishe/icons/icon-512x512.png'
];

// 安装事件 - 缓存资源
self.addEventListener('install', function(event) {
  console.log('Service Worker installing...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
      .then(function() {
        console.log('All resources cached successfully');
        return self.skipWaiting();
      })
      .catch(function(error) {
        console.log('Cache failed:', error);
      })
  );
});

// 激活事件 - 清理旧缓存
self.addEventListener('activate', function(event) {
  console.log('Service Worker activating...');
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(function() {
      console.log('Service Worker activated');
      return self.clients.claim();
    })
  );
});

// 获取事件 - 缓存优先策略
self.addEventListener('fetch', function(event) {
  console.log('Fetching:', event.request.url);
  
  // 只处理GET请求
  if (event.request.method !== 'GET') {
    return;
  }
  
  // 跳过非HTTP请求
  if (!event.request.url.startsWith('http')) {
    return;
  }
  
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // 如果缓存中有响应，返回缓存的响应
        if (response) {
          console.log('Serving from cache:', event.request.url);
          return response;
        }
        
        // 否则从网络获取
        console.log('Fetching from network:', event.request.url);
        return fetch(event.request)
          .then(function(response) {
            // 检查响应是否有效
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            
            // 克隆响应，因为响应流只能使用一次
            var responseToCache = response.clone();
            
            // 缓存新的响应
            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
                console.log('Cached new resource:', event.request.url);
              });
            
            return response;
          })
          .catch(function(error) {
            console.log('Fetch failed:', error);
            
            // 如果是HTML页面，返回离线页面
            if (event.request.headers.get('accept').includes('text/html')) {
              return caches.match('/tanchishe/snake_mobile_wechat_fullscreen_pwa.html');
            }
          });
      })
  );
});

// 推送事件 - 处理推送通知
self.addEventListener('push', function(event) {
  console.log('Push event received');
  
  if (event.data) {
    const data = event.data.json();
    const options = {
      body: data.body || '来玩贪吃蛇游戏吧！',
      icon: '/tanchishe/icons/icon-192x192.png',
      badge: '/tanchishe/icons/icon-72x72.png',
      vibrate: [100, 50, 100],
      data: {
        dateOfArrival: Date.now(),
        primaryKey: 1
      },
      actions: [
        {
          action: 'explore',
          title: '开始游戏',
          icon: '/tanchishe/icons/icon-96x96.png'
        },
        {
          action: 'close',
          title: '关闭',
          icon: '/tanchishe/icons/icon-96x96.png'
        }
      ]
    };
    
    event.waitUntil(
      self.registration.showNotification('贪吃蛇游戏', options)
    );
  }
});

// 通知点击事件
self.addEventListener('notificationclick', function(event) {
  console.log('Notification clicked');
  
  event.notification.close();
  
  if (event.action === 'explore') {
    // 用户点击了"开始游戏"
    event.waitUntil(
      clients.openWindow('/tanchishe/snake_mobile_wechat_fullscreen_pwa.html')
    );
  } else if (event.action === 'close') {
    // 用户点击了"关闭"
    console.log('Notification closed by user');
  } else {
    // 用户点击了通知本身
    event.waitUntil(
      clients.matchAll({type: 'window'}).then(function(clientList) {
        // 如果已经有窗口打开，聚焦到该窗口
        for (let i = 0; i < clientList.length; i++) {
          const client = clientList[i];
          if (client.url.includes('/tanchishe/') && 'focus' in client) {
            return client.focus();
          }
        }
        // 如果没有窗口打开，打开新窗口
        if (clients.openWindow) {
          return clients.openWindow('/tanchishe/snake_mobile_wechat_fullscreen_pwa.html');
        }
      })
    );
  }
});

// 同步事件 - 后台同步
self.addEventListener('sync', function(event) {
  console.log('Background sync event:', event.tag);
  
  if (event.tag === 'background-sync') {
    event.waitUntil(
      // 这里可以执行后台同步任务
      console.log('Background sync completed')
    );
  }
});

// 消息事件 - 处理来自主线程的消息
self.addEventListener('message', function(event) {
  console.log('Message received in Service Worker:', event.data);
  
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'GET_VERSION') {
    event.ports[0].postMessage({version: CACHE_NAME});
  }
});

// 错误处理
self.addEventListener('error', function(event) {
  console.error('Service Worker error:', event.error);
});

// 未处理的Promise拒绝
self.addEventListener('unhandledrejection', function(event) {
  console.error('Unhandled promise rejection:', event.reason);
}); 
/* Start the app after every view file has loaded. */
'use strict';
applyTheme(); loadMock(); render();
initCloud().then(()=>DICT.init()).catch(()=>{});

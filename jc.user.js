// ==UserScript==
// @name         自动机惨系统
// @namespace    https://www.d0j1a1701.cc
// @version      0.1
// @description  IAKIOI!
// @author       d0j1a_1701
// @match        https://www.luogu.com.cn/
// @icon         https://www.google.com/s2/favicons?domain=luogu.com.cn
// @grant        none
// ==/UserScript==

let words = ['I AK IOI','我在此郑重宣布 I AK IOI','洛谷将会臭名昭著!','我将在三天之内撕碎洛谷脆弱的防火墙!','我AK5次IOI!']

(function() {
    'use strict';
    document.getElementById('feed-content').value = words[Math.floor(Math.random()*words.length)];
    document.getElementById('feed-submit').click();
    // Your code here...
})();

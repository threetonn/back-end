"use strict";(self["webpackChunktriton"]=self["webpackChunktriton"]||[]).push([[6304],{6304:function(e,a,r){r.r(a),r.d(a,{default:function(){return h}});var s=r(3396),t=r(7139);const i={class:"profile-page"},n=(0,s._)("h1",{class:"profile-page__title"},"Персонал",-1),c={class:"profile-page__trainer-cards"},l={class:"trainer-card__title"},o=["src"],f=["onClick"];function d(e,a,r,d,u,g){return(0,s.wg)(),(0,s.iD)("div",i,[n,(0,s._)("div",c,[((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(d.staffs,(e=>((0,s.wg)(),(0,s.iD)("div",{class:"trainer-card",key:e.email},[(0,s._)("p",l,(0,t.zw)(e.name+" "+e.surname),1),e.image?((0,s.wg)(),(0,s.iD)("img",{key:0,class:"trainer-card__image",src:e.image},null,8,o)):((0,s.wg)(),(0,s.iD)(s.HY,{key:1},[(0,s.Uk)(" Нет изображения ")],64)),(0,s._)("button",{class:"trainer-card__show-btn",onClick:a=>d.showTrainerInfo(e.email)},null,8,f)])))),128))])])}var u=r(65),g={setup(){const e=(0,u.oR)(),a=(0,s.Fl)((()=>e.getters.getStaff));(0,s.wF)((()=>{a.value||e.dispatch("getStaff")}));const r=r=>{e.dispatch("showUserCard"),e.dispatch("selectUser",a.value.find((e=>e.email==r)))},t=()=>{e.dispatch("hideUserCard")};return{staffs:a,showTrainerInfo:r,closeTrainerInfo:t}}},p=r(89);const _=(0,p.Z)(g,[["render",d]]);var h=_}}]);
//# sourceMappingURL=6304.b5ac6212.js.map
"use strict";(self["webpackChunktriton"]=self["webpackChunktriton"]||[]).push([[2996,4336,6030],{6030:function(s,t,e){function i(s,t,e,i){let a=Math.abs(s);return a%=100,a>=5&&a<=20?i:(a%=10,1===a?t:a>=2&&a<=4?e:i)}e.r(t),e.d(t,{getNoun:function(){return i}})},4336:function(s,t,e){e.r(t),e.d(t,{default:function(){return V}});var i=e(3396),a=e(7139),r=e(9242);const n={class:"subscription-card__text-block"},c={class:"subscription-card__title"},u={class:"subscription-card__price-month"},o={class:"price"},l=(0,i._)("span",null,"руб./день",-1),p=(0,i._)("p",{class:"subscription-card__price-year--description"}," При оплате за год: ",-1),d={class:"subscription-card__price-year"},b={class:"price"},_=(0,i._)("span",null,"руб./за",-1),D={class:"days"},w={class:"discount"},g={class:"subscription-card__list"},v=(0,i._)("svg",{width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg"},[(0,i._)("path",{d:"M4 12L10 18L20 6",stroke:"black","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round"})],-1),y={class:"subscription-card__sub-date"},h=(0,i._)("span",null,"Начало: ",-1),f={class:"error-msg"},k={class:"error-msg"},S=["disabled"];function m(s,t,e,m,$,C){return(0,i.wg)(),(0,i.iD)("div",{class:(0,a.C_)(["subscription-card",`subscription-card--${e.subscription.type}`])},[(0,i._)("div",null,[(0,i._)("div",n,[(0,i._)("p",c,(0,a.zw)(e.subscription.title),1),(0,i._)("p",u,[(0,i._)("span",o,(0,a.zw)(e.subscription.price),1),l]),(0,i._)("div",null,[p,(0,i._)("p",d,[(0,i._)("span",b,(0,a.zw)(m.subscriptioDiscountCalculation(e.subscription.price*m.state.subscriptionDays)),1),_,(0,i._)("span",D,(0,a.zw)(m.state.subscriptionDays),1),(0,i._)("span",null,(0,a.zw)(m.getNoun(m.state.subscriptionDays,"день","дня","дней")),1)]),(0,i._)("p",w,[(0,i.Uk)(" Скидка: "),(0,i._)("span",null,(0,a.zw)((100*m.computedDiscount).toFixed(2))+"%",1)])])]),(0,i._)("ul",g,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(e.subscription.features,((s,t)=>((0,i.wg)(),(0,i.iD)("li",{class:"subscription-card__list-item",key:t},[v,(0,i._)("span",null,(0,a.zw)(s),1)])))),128))])]),(0,i._)("div",null,[(0,i._)("div",y,[(0,i._)("div",null,[(0,i._)("div",{class:(0,a.C_)(["lf-inputs__wrapper",{error:m.v$.subStartDate.$errors.length}])},[h,(0,i.wy)((0,i._)("input",{"onUpdate:modelValue":t[0]||(t[0]=s=>m.state.subStartDate=s),class:"subscription-card__date-input",type:"date"},null,512),[[r.nr,m.state.subStartDate]]),((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(m.v$.subStartDate.$errors,(s=>((0,i.wg)(),(0,i.iD)("div",{class:"input-errors",key:s.$uid},[(0,i._)("div",f,(0,a.zw)(s.$message),1)])))),128))],2)]),(0,i._)("p",null,"Конец: "+(0,a.zw)(m.endDate.toLocaleDateString()),1)]),(0,i._)("div",{class:(0,a.C_)(["lf-inputs__wrapper",{error:m.v$.subscriptionDays.$errors.length}])},[(0,i.wy)((0,i._)("input",{class:"subscription-card__days-input",type:"number",name:"sub-data",autocomplete:"off",placeholder:"Дни абонемента","onUpdate:modelValue":t[1]||(t[1]=s=>m.state.subscriptionDays=s)},null,512),[[r.nr,m.state.subscriptionDays,void 0,{number:!0}]]),((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(m.v$.subscriptionDays.$errors,(s=>((0,i.wg)(),(0,i.iD)("div",{class:"input-errors",key:s.$uid},[(0,i._)("div",k,(0,a.zw)(s.$message),1)])))),128))],2),(0,i._)("button",{onClick:t[2]||(t[2]=s=>m.activateSubscription(e.subscription.id)),class:(0,a.C_)(["subscription-card__button",m.isValid&&"disabled"]),disabled:m.isValid}," Активировать ",10,S)])],2)}var $=e(4870),C=e(6030),z=e(3053),F=e(9117),M={props:{subscription:Object,callback:Function},setup(s){const t=(0,$.qj)({subscriptionDays:1,subStartDate:null}),e=(0,i.Fl)((()=>t.subscriptionDays*s.subscription.discount/100)),a=s=>Math.round(s-s*e.value),r=(0,$.iH)(!1),n=new Date,c=(0,$.iH)(new Date((new Date).setDate((new Date).getDate()+t.subscriptionDays))),u=s=>new Date((new Date).setDate((new Date).getDate()+30))>=new Date(s)&&new Date(s)>=new Date,o=(0,i.Fl)((()=>({subscriptionDays:{required:F.helpers.withMessage("Поле обязательно для заполнения",F.required),between:F.helpers.withMessage("Абонемент не может быть меньше 1 и больше 365 дней",(0,F.between)(1,365))},subStartDate:{required:F.helpers.withMessage("Необходимо выбрать дату!",F.required),maxDateValidator:F.helpers.withMessage("Максимально отложить дату можно на 30 дней!",u)}}))),l=(0,z.Xw)(o,t),p=()=>(l.value.$touch(),l.value.$errors.length?(r.value=!0,console.log("Невалидно")):(r.value=!1,console.log("Валидно")));(0,i.YP)((()=>[t.subscriptionDays,t.subStartDate]),(()=>{p(),c.value=new Date(new Date(t.subStartDate).setDate(new Date(t.subStartDate).getDate()+t.subscriptionDays))}));const d=e=>{p();const i={id:e,start_date:t.subStartDate,day_count:t.subscriptionDays};!r.value&&s.callback(i)};return{state:t,v$:l,getNoun:C.getNoun,currentDate:n,endDate:c,isValid:r,subscriptioDiscountCalculation:a,computedDiscount:e,activateSubscription:d}}},H=e(89);const N=(0,H.Z)(M,[["render",m]]);var V=N},2996:function(s,t,e){e.r(t),e.d(t,{default:function(){return _}});var i=e(3396);const a={class:"profile-page"},r=(0,i._)("h1",{class:"profile-page__title"},"Абонементы",-1),n={class:"profile-page__subscriptions"};function c(s,t,e,c,u,o){const l=(0,i.up)("TTCardSubscription");return(0,i.wg)(),(0,i.iD)("div",a,[r,(0,i._)("div",n,[((0,i.wg)(!0),(0,i.iD)(i.HY,null,(0,i.Ko)(c.subscriptionsCards,(s=>((0,i.wg)(),(0,i.j4)(l,{key:s.id,subscription:s,callback:s=>c.activateSubscription(s)},null,8,["subscription","callback"])))),128))])])}var u=e(4336),o=e(65),l=e(4030),p={components:{TTCardSubscription:u["default"]},setup(){const s=(0,o.oR)(),t=(0,i.Fl)((()=>s.getters.getSubscriptionCards)),e=(0,i.Fl)((()=>s.getters.getTokens)),a=(0,i.Fl)((()=>s.getters.getUserSubscription)),r=t=>{try{const i={id:t.id,access_token:e.value.access_token,start_date:t.start_date,day_count:t.day_count};a.value,s.dispatch("setUserSubscription",i),(0,l.successNotify)("Абонемент обновлен")}catch(i){throw(0,l.errorNotify)("Ошибка обновления абонемента!"),new Error(i)}};return{subscriptionsCards:t,activateSubscription:r}}},d=e(89);const b=(0,d.Z)(p,[["render",c]]);var _=b}}]);
//# sourceMappingURL=2996.e16aaee5.js.map
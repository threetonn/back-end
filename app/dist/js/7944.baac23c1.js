"use strict";(self["webpackChunktriton"]=self["webpackChunktriton"]||[]).push([[7944,4969],{7944:function(e,a,r){r.r(a),r.d(a,{default:function(){return q}});var n=r(3396),l=r(7139),d=r(9242),t=r(4969);const s={class:"base-inputs__radio-wrapper"},i={class:"gender"},u=(0,n._)("span",{class:"gender__text"},"Пол:",-1),c={class:"gender__group"},g=["checked"],o=(0,n._)("label",{for:"male"},"Муж.",-1),p={class:"gender__group"},_=["checked"],v=(0,n._)("label",{for:"female"},"Жен.",-1),f={class:"error-msg"},m=["disabled"],b=(0,n._)("img",{src:t,alt:"save"},null,-1),h=[b];function k(e,a,r,t,b,k){return(0,n.wg)(),(0,n.iD)("div",s,[(0,n._)("div",{class:(0,l.C_)(["base-inputs__wrapper",{error:t.v$.gender.$errors.length}])},[(0,n._)("div",i,[u,(0,n._)("div",c,[(0,n.wy)((0,n._)("input",{class:"gender__input",type:"radio",id:"male",name:"radio-group",value:"male",checked:"male"===t.state.gender?.en,"onUpdate:modelValue":a[0]||(a[0]=e=>t.state.gender=e)},null,8,g),[[d.G2,t.state.gender]]),o]),(0,n._)("div",p,[(0,n.wy)((0,n._)("input",{class:"gender__input",type:"radio",id:"female",name:"radio-group",value:"female",checked:"female"===t.state.gender?.en,"onUpdate:modelValue":a[1]||(a[1]=e=>t.state.gender=e)},null,8,_),[[d.G2,t.state.gender]]),v])]),((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(t.v$.gender.$errors,(e=>((0,n.wg)(),(0,n.iD)("div",{class:"input-errors",key:e.$uid},[(0,n._)("div",f,(0,l.zw)(e.$message),1)])))),128))],2),(0,n._)("button",{class:(0,l.C_)(["base-inputs__button",!t.fieldValidated&&"disabled"]),onClick:a[2]||(a[2]=(0,d.iM)(((...e)=>t.changeData&&t.changeData(...e)),["prevent"])),disabled:!t.fieldValidated},h,10,m)])}var w=r(4870),$=r(3053),D=r(9117),y={props:{gender:String,callback:Function,fieldName:String},setup(e){const a=(0,w.iH)(!1),r=(0,w.qj)({gender:e.gender||null}),l=(0,n.Fl)((()=>({gender:{required:D.helpers.withMessage("Не выбран пол",D.required)}}))),d=(0,$.Xw)(l,r),t=()=>{if(d.value.$touch(),d.value.$invalid)return a.value=!1;a.value=!0};(0,n.YP)((()=>r.gender),(()=>t()));const s=()=>{d.value.$invalid||e.callback({[e.fieldName]:r.gender})};return{v$:d,state:r,fieldValidated:a,changeData:s}}},C=r(89);const V=(0,C.Z)(y,[["render",k]]);var q=V},4969:function(e,a,r){e.exports=r.p+"img/save.78fe2e16.png"}}]);
//# sourceMappingURL=7944.baac23c1.js.map
(this.webpackJsonptweeter=this.webpackJsonptweeter||[]).push([[0],{15:function(e,t,a){e.exports=a(29)},20:function(e,t,a){},28:function(e,t,a){},29:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),s=a(2),o=a.n(s),c=(a(20),a(9)),l=a(10),i=a(14),d=a(13),m=a(3),u=(a(27),a(28),function(e){Object(i.a)(a,e);var t=Object(d.a)(a);function a(e){var n;return Object(c.a)(this,a),(n=t.call(this,e)).state={data:[]},n}return Object(l.a)(a,[{key:"componentDidMount",value:function(){var e=this;this.props.addTodo(),setTimeout((function(){e.setState({data:e.props.todos})}),5e3)}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"product-list-wrapper"},this.state.data.length<1?r.a.createElement("div",{className:"row spinner_cls"},r.a.createElement("div",{className:"spinner-border text-primary",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading...")),r.a.createElement("div",{className:"spinner-border text-secondary",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading...")),r.a.createElement("div",{className:"spinner-border text-success",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading...")),r.a.createElement("div",{className:"spinner-border text-danger",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading...")),r.a.createElement("div",{className:"spinner-border text-warning",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading...")),r.a.createElement("div",{className:"spinner-border text-info",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading...")),r.a.createElement("div",{className:"spinner-border text-light",role:"status"},r.a.createElement("span",{className:"sr-only"},"Loading..."))):r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col-6"},r.a.createElement("table",{className:"table"},r.a.createElement("thead",{className:"thead-dark"},r.a.createElement("tr",null,r.a.createElement("th",{scope:"col"},"#"),r.a.createElement("th",{scope:"col"},"Tweet"))),r.a.createElement("tbody",null,this.state.data.data.map((function(e,t){return r.a.createElement("tr",{key:t},r.a.createElement("th",{scope:"row"},t+1),r.a.createElement("td",null,e.title))}))))),r.a.createElement("div",{className:"col-6 button_css"},r.a.createElement("button",{className:"btn btn-primary",onClick:function(){return e.props.addTodo()}},"Fetch New Tweets"))))}}]),a}(n.Component)),p=Object(m.b)((function(e){return{todos:e.id}}),(function(e){return{addTodo:function(){return e((function(e){fetch("http://127.0.0.1:8000/api/tweets",{method:"GET",redirect:"follow"}).then((function(e){return e.json()})).then((function(t){return e({type:"ADD_TODO",id:t})})).catch((function(e){return console.log("error",e)}))}))}}}))(u);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var h=a(1),E=a(12),v=a(7),b=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"ADD_TODO":return Object(v.a)(Object(v.a)({},e),{},{id:t.id});default:return e}},f=Object(h.c)(b,Object(h.a)(E.a));o.a.render(r.a.createElement(m.a,{store:f},r.a.createElement(p,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[15,1,2]]]);
//# sourceMappingURL=main.fa43a04a.chunk.js.map
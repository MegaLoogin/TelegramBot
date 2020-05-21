var sse_source = null;
let xhr = new XMLHttpRequest();
xhr.open("GET", "https://charts.forexpf.ru/html/htmlquotes/q");
var time = null;
xhr.onload = function()
{
	time = new Date().getTime();
	let xhr2 = new XMLHttpRequest();
	console.log(1, xhr.responseText);
	xhr2.open("GET", "https://charts.forexpf.ru/html/htmlquotes/q?msg=1;SID=" + xhr.responseText + ";T=" + new Date().getTime());

	xhr2.onload = function(){
		console.log(2, xhr2);
	}	
	xhr2.send(null);
	sse_source = new EventSource('/html/htmlquotes/qsse?msg=1;SID=' + xhr.responseText + ";T=" + time);
	sse_source.onmessage = function(e) { console.log(e)}
}	
xhr.send(null)


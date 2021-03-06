﻿var myPictures = ["Example1.png", "Example2.png", "Example3.png", "Example4.png"];
var howMany = myPictures.length - 1;
var number = 1;

var v_events;           

function chgImg() {
	var slide = document.getElementById("myImage");
	slide.src = myPictures[number];
	(number < howMany) ? number++ : number=0;
}
setInterval(function(){chgImg()},4000);

function link(ref, showEve) {
    document.getElementById("content").innerHTML = getLink(ref);
    if(showEve != "start") {
	check = elementClicked(showEve);
	if(check.className == "show") {
	    document.getElementById('slideshow').style.display = "";
	} else {
	    document.getElementById('slideshow').style.display = "none";
	}
    }
}

//	<p class='event'>Mar-15-2015-Sunday 10:00AM-2:00PM</p></div> \
function getLink(ref) {
	var link =     
		"<h1> Celia's Vision Statement </h1> \
		<p> By thoroughly educating, guiding and escorting individuals, \
		we help them to become educated investors who can secure their financial futures \
		in retirement and children's education by building long-term sustaining wealth \
		through the art and science of landbanking. </p><br> \
    	<p> 培育、訓練更多的精英成為投資土地的專材，\
		讓這些專家中的嬴家們能用他們的專業知識和經驗去㨍助更多的普通人去投資一些精挑細選過、\
		最具發展潛力的重點地，利用時間的變化和人潮的走向得以致富。 </p><br> \
		<p> ~能像一盞燈去照亮他人的前途是我的義務也是一份榮幸~ </p>";
	if (ref == 1) {
		link = "<div id='events'><h1> Upcoming Events </h1> \
                <div>Please register to reserve, as seating is limited - those not registered will not be guaranteed a seat. \
Click on the event date to register: </div> \
		<p class='event'>April-23-2016-Saturday 1:00PM-5:00PM</p> \
                <p class='event'>April-24-2016-Sunday 10:00AM-2:00PM</p> \
		<div>Velur Vice President, Celia Pan will give a Chinese seminar with updated information that will help you understand the current investment market.</div><br>";
	}
	if (ref == 2) {
		link = "<div id='articles'><h1> Frequently Asked Questions </h1>\
		<p class='article1'> 1. What is \"Land Banking\"? (Chinese) </p>\
		<p class='article2'> 2. When is the right time for me? (Chinese) </p>\
		<p class='article3'> 3. How do I protect my rights? (Chinese) </p>\
		<p class='article4'> 4. What are the differences between buying land and buying a house? (Chinese) </p>\
		<p class='article5'> 5. Why should I consider Velur Enterprises? (English)</p></div>";
	}
	if (ref == 3) {
		link = "<h1> Celia's Biography </h1>\
    	<h2> Ms. Celia Pan </h2>\
		<p> •	30 Years of Phenomenal Experience in Real Estate </p>\
		<p> •	Trained hundreds of landbanking  professionals in Southern California </p>\
		<p> •	Has achieved one of the highest ranks in company history </p>\
		<p> •	Responsible for several hundred million dollars of transactions </p>\
		<p> •	Highlighted and spoken in National Real Estate Forums </p>\
		<p> •	Writer of Investment Articles for the Chinese Daily News </p>\
		<p> •	Recently Featured in the Cover of China Fortune Magazine </p><br> \
		<h2> 潘美霖女士</h2> \
		<p> •	加州著名土地经营专家，华人富豪。有30余年土地开发和买卖经验， 美国伟洛土地银行公司副总裁。 </p>\
		<p> •	負責訓練培養南加卅百萬經紀成土地專業人材 </p>\
		<p> •	以数亿美元经营业绩在伟洛公司历史上获得最高头衔 </p>\
		<p> •	曾为世界日报投资理财专栏撰写文章 </p>\
		<p> •	洛杉矶地区华语广播电台和电视台投资理财节目特请讲员 </p>\
		<p> •	曾经引领多位普通华人在土地投资中致富 </p>\
		<p> •	《中国财富杂志》封面人物 </p>";
	}
	if (ref == 4) {
		link = "<h1> Velur Enterprises, Inc. </h1>\
		<p> 偉洛土地投資發展公司 </p><br>\
                <h2> Headquarter </h2>\
		<p> 5990 Sepulveda Blvd, Van Nuys, CA 91411 </p><br>\
		<h2> Rowland Heights Office </h2>\
                <p> 17800 Castleton St, City Of Industry, CA 91748 </p><br>\
                <h2> Velur Silicon Valley Office </h2>\
                <p> 145 South Main Street suite #145, Milpitas, CA 95035</p>\
                <p> Email: celiacpan@gmail.com </p>\
                <p> Telephone: 1-888-363-4838 </p>";
	}
	return link;
}

function openForm(theEvent) {
	target = elementClicked(theEvent);
	elementValue = target.innerHTML;
	if(target.className != 0) {
		if(document.getElementById('newTab') == null) {
			var d = document.createElement("div");
			d.id = "newTab"; 
			if(target.className == "event") {
				loadDoc(d, "form.html");
				d.innerHTML = d.innerHTML.replace("changeThis", elementValue); 
			} else if(target.className == "article1") {
				loadDoc(d, "Land Banker.htm");
			} else if(target.className == "article2") {
				loadDoc(d, "Entry Point.htm");
			} else if(target.className == "article3") {
				loadDoc(d, "Protect Rights.htm");
			} else if(target.className == "article4") {
				loadDoc(d, "Land vs House.htm");
			} else if(target.className == "article5") {
				loadDoc(d, "Why Velur.htm");
			} 
			target.appendChild(d);
		} else if(target.className != 'invalid') {
			current = document.getElementById('newTab').parentNode;
			current.removeChild(document.getElementById('newTab'));
			if(target.firstChild != current.firstChild) {
				openForm(theEvent);
			} 
		}
	}
}

function elementClicked(e) {
	var targ;
	if (!e) var e = window.event;
	if (e.target) targ = e.target;
	else if (e.srcElement) targ = e.srcElement;
	if (targ.nodeType == 3) // defeat Safari bug
		targ = targ.parentNode;
	return targ;
}

function loadDoc(ele, url) {
	var xhr=false;
	/*@cc_on @*/
	/*@if (@_jscript_version >= 5)
	// JScript gives us Conditional compilation, we can cope with old IE versions.
	// and security blocked creation of the objects.
	try {
		xhr = new ActiveXObject("Msxml2.XMLHTTP");
	} catch (e) {
		try {
			xhr = new ActiveXObject("Microsoft.XMLHTTP");
		} catch (E) {
			xhr = false;
		}
	}
	@end @*/
	if (!xhr && typeof XMLHttpRequest!='undefined') {
		try {
			xhr = new XMLHttpRequest();
		} catch (e) {
			xhr = false;
		}
	}
	xhr.open("GET", url, false); //synchronous
	xhr.send(null);
	ele.innerHTML=xhr.responseText;
}



function vali() {
	//$.tools.validator.conf.position = "center";
	//$.tools.validator.conf.offset = [-75,0];
	if ($.browser.msie && $.browser.version < 10) {
		$("#upro").validator();
	}
	if ($.browser.safari) {
		$('#upro[required]').addClass('required').removeAttr('required');
		var inputs = $("#upro").validator();
		return inputs.data("validator").checkValidity(); //true, false
	}
}

$(document).ready(function() {       
       $.ajax({
                type: 'GET',
                url: '../GetEvents/events.json',
                data: { get_param: 'value'},
                dataType: 'json',
                complete: function(data){
                    v_events = $.parseJSON(data.responseText);
		    console.log(v_events[0].event_date);
                }
       });
});

$(document).ajaxComplete(function(){            
    v_events = $.parseJSON(v_events.responseText); //Takes AJAX Reponse Text and parses it to JSON
    console.log(v_events);
});

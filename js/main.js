//Read txt files 
function readFile(txtfilename) {
    jQuery.get(txtfilename,function(txt){
       var obj=$('#outputtp').text(txt); 
       obj.html(obj.html().replace(/\n/g,'<br/>'))
    });
}    

function readFile1(txtfilename) {
    jQuery.get(txtfilename,function(txt){
       var obj=$('#outputtc').text(txt); 
       obj.html(obj.html().replace(/\n/g,'<br/>'))
    });
}    

function readFile2(txtfilename) {
    jQuery.get(txtfilename,function(txt){
       var obj=$('#outputtt').text(txt); 
       obj.html(obj.html().replace(/\n/g,'<br/>'))
    });
}    

//toggle bar charts
function toggleimage1() {
  var a = document.getElementById("image1");
  var b = document.getElementById("image2");
  var c = document.getElementById("image3");
  var d = document.getElementById("image4");
  var e = document.getElementById("image5");
  a.style.display="block";
  a.style.animation="appear 1s";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
}

function toggleimage2() {
  var a = document.getElementById("image1");
  var b = document.getElementById("image2");
  var c = document.getElementById("image3");
  var d = document.getElementById("image4");
  var e = document.getElementById("image5");
  a.style.display="none";
  b.style.display="block";
  b.style.animation="appear 1s";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
}

function toggleimage3() {
  var a = document.getElementById("image1");
  var b = document.getElementById("image2");
  var c = document.getElementById("image3");
  var d = document.getElementById("image4");
  var e = document.getElementById("image5");
  a.style.display="none";
  b.style.display="none";
  c.style.display="block";
  c.style.animation="appear 1s";
  d.style.display="none";
  e.style.display="none";
}

function toggleimage4() {
  var a = document.getElementById("image1");
  var b = document.getElementById("image2");
  var c = document.getElementById("image3");
  var d = document.getElementById("image4");
  var e = document.getElementById("image5");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="block";
  d.style.animation="appear 1s";
  e.style.display="none";
}

function toggleimage5() {
  var a = document.getElementById("image1");
  var b = document.getElementById("image2");
  var c = document.getElementById("image3");
  var d = document.getElementById("image4");
  var e = document.getElementById("image5");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="block";
  e.style.animation="appear 1s";
}

function toggleimaget1() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="block";
  a.style.animation="appear 1s";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
  f.style.display="none";
  g.style.display="none";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget2() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="block";
  b.style.animation="appear 1s";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
  f.style.display="none";
  g.style.display="none";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget3() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="block";
  c.style.animation="appear 1s";
  d.style.display="none";
  e.style.display="none";
  f.style.display="none";
  g.style.display="none";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget4() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="block";
  d.style.animation="appear 1s";
  e.style.display="none";
  f.style.display="none";
  g.style.display="none";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget5() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="block";
  e.style.animation="appear 1s";
  f.style.display="none";
  g.style.display="none";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget6() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
  f.style.display="block";
  f.style.animation="appear 1s";
  g.style.display="none";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget7() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
  f.style.display="none";
  g.style.display="block";
  g.style.animation="appear 1s";
  h.style.display="none";
  i.style.display="none";
}

function toggleimaget8() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
  f.style.display="none";
  g.style.display="none";
  h.style.display="block";
  h.style.animation="appear 1s";
  i.style.display="none";
}

function toggleimaget9() {
  var a = document.getElementById("imaget1");
  var b = document.getElementById("imaget2");
  var c = document.getElementById("imaget3");
  var d = document.getElementById("imaget4");
  var e = document.getElementById("imaget5");
  var f = document.getElementById("imaget6");
  var g = document.getElementById("imaget7");
  var h = document.getElementById("imaget8");
  var i = document.getElementById("imaget9");
  a.style.display="none";
  b.style.display="none";
  c.style.display="none";
  d.style.display="none";
  e.style.display="none";
  f.style.display="none";
  g.style.display="none";
  h.style.display="none";
  i.style.display="block";
  i.style.animation="appear 1s";
}

//Background effect
particlesJS("snowfall", {
  "particles": {
    "number": {
      "value": 100
    },
    "color": {
  "value": "#fff"
},
    "shape": {
  "type": "circle",
  "stroke": {
     "width": .5,
     "color": "transparent"
  },
  "polygon": {
     "nb_sides": 6
  }
},
    "size": {
      "value": 5,
      "random": true
    },
       "opacity": {
      "value": 0.5,
      
    },
    "line_linked": {
      "enable": true
    },
    "move": {
      "enable": true,
      "speed": 5
    }
  },

  "interactivity": {
    "detect_on": "canvas",
    "events": {
      "onhover": {
        "enable": true
      }
    },
      "events": {
  "onhover": {
    "enable": true,
    "mode": "repulse"
  },
  "onclick": {
    "enable": true,
    "mode": "push"
  },
    "resize": true
}
  }
});

//Scroll down button on panel 1
var scrollY = 0;
var distance = 0;
var speed = 0;
function autoScrollTo(el) {
	var currentY = (window.pageYOffset)+106;
	var targetY = document.getElementById(el).offsetTop;
	var bodyHeight = document.body.offsetHeight;
	var yPos = currentY + window.innerHeight;
	var animator = setTimeout('autoScrollTo(\''+el+'\')',30);
	if(yPos > bodyHeight){
		clearTimeout(animator);
	} else {
		if(currentY < targetY-distance){
		    scrollY = currentY+distance;
		    window.scroll(0, scrollY);
	    } else {
		    clearTimeout(animator);
	    }
	}
}
function resetScroller(el){
	var currentY = window.pageYOffset;
    var targetY = document.getElementById(el).offsetTop;
	var animator = setTimeout('resetScroller(\''+el+'\')',speed);
	if(currentY > targetY){
		scrollY = currentY-distance;
		window.scroll(0, scrollY);
	} else {
		clearTimeout(animator);
	}
}

//Pin navigation bar
$(document).ready(function(){
  $('body').scrollspy({target: ".navi", offset: 50}); 
  $("#myNavbar a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    } 
  });
});

$(document).ready(function(){
    
//Scroll animations
var controller = new ScrollMagic.Controller();
    
var pinaboutmeScene = new ScrollMagic.Scene({
    triggerElement: '.main',
    triggerHook: 0
})    
.setPin('.main',{pushFollowers:false})
.addTo(controller);    
    
var pinnavScene = new ScrollMagic.Scene({
    triggerElement: '#navi',
    triggerHook: 0.099 //or else the content is seen between h1 and navi
})    
.setPin('#navi',{pushFollowers:false})
.addTo(controller);
 
var scene = new ScrollMagic.Scene({triggerElement:".quote", triggerHook:.6,duration: 1000})  
.setClassToggle('.quote h2','fade-in-left')
.addTo(controller);    

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel2 h2"),1,{opacity:0, scale:3}))
    .add(TweenMax.from(("#panel2 p"),1,{opacity:0, scale:1.5}))
    .from('#panel2 .pricepoint', 1, {x: '-150%', delay:1, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel2', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie0", triggerHook:.8})  
.setClassToggle('#panel2 .pricepie0','pricepie0_2')
scene.reverse(false)
.addTo(controller);  
            
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie1", triggerHook:.7})  
.setClassToggle('#panel2 .pricepie1','pricepie1_2')
scene.reverse(false)
.addTo(controller);  
        
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie2", triggerHook:.65})  
.setClassToggle('#panel2 .pricepie2','pricepie2_2')
scene.reverse(false)
.addTo(controller);  
            
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie3", triggerHook:.6})  
.setClassToggle('#panel2 .pricepie3','pricepie3_2')
scene.reverse(false)
.addTo(controller);  
                
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie4", triggerHook:.55})  
.setClassToggle('#panel2 .pricepie4','pricepie4_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie5", triggerHook:.5})  
.setClassToggle('#panel2 .pricepie5','pricepie5_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie6", triggerHook:.45})  
.setClassToggle('#panel2 .pricepie6','pricepie6_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie7", triggerHook:.4})  
.setClassToggle('#panel2 .pricepie7','pricepie7_2')
scene.reverse(false)
.addTo(controller);    
    
var scene = new ScrollMagic.Scene({triggerElement:"#panel2 .pricepie8", triggerHook:.35})  
.setClassToggle('#panel2 .pricepie8','pricepie8_2')
scene.reverse(false)
.addTo(controller);  

var timeline = new TimelineMax()
    .from('#panel2 .infer', 0.5, {x: '100%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel2 #outputtp', 0.5, {x: '-100%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel2 h3', triggerHook:.7})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);
             
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel3 h2"),1,{opacity:0, scale:3}))
    .add(TweenMax.from(("#panel3 .types"),1,{opacity:0, scale:0}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel3 .pricepoint', triggerHook:.9})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel3 p"),1,{opacity:0, scale:1.5}))
    .from('#panel3 .pricepoint', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel3 .pricepoint', triggerHook:.4})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);
    
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie0", triggerHook:.8})  
.setClassToggle('#panel3 .pricepie0','pricepie0_2')
scene.reverse(false)
.addTo(controller);  
            
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie1", triggerHook:.7})  
.setClassToggle('#panel3 .pricepie1','pricepie1_2')
scene.reverse(false)
.addTo(controller);  
        
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie2", triggerHook:.65})  
.setClassToggle('#panel3 .pricepie2','pricepie2_2')
scene.reverse(false)
.addTo(controller);  
            
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie3", triggerHook:.6})  
.setClassToggle('#panel3 .pricepie3','pricepie3_2')
scene.reverse(false)
.addTo(controller);  
                
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie4", triggerHook:.55})  
.setClassToggle('#panel3 .pricepie4','pricepie4_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie5", triggerHook:.5})  
.setClassToggle('#panel3 .pricepie5','pricepie5_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie6", triggerHook:.45})  
.setClassToggle('#panel3 .pricepie6','pricepie6_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie7", triggerHook:.4})  
.setClassToggle('#panel3 .pricepie7','pricepie7_2')
scene.reverse(false)
.addTo(controller);    
    
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie8", triggerHook:.35})  
.setClassToggle('#panel3 .pricepie8','pricepie8_2')
scene.reverse(false)
.addTo(controller);  
        
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .button0", triggerHook:.7})  
.setClassToggle('#panel3 .button0','button0_2')
scene.reverse(false)
.addTo(controller);  

var tween = TweenMax.to(".button1", 1, {opacity:1, scale: 1});
var scene = new ScrollMagic.Scene({triggerElement:"#panel3 .pricepie8", triggerHook:.0})  
.setTween(tween)
.addTo(controller);

var timeline = new TimelineMax()
    .from('#panel3 #image1', 1, {x: '-100%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel3 #image1', triggerHook:.5})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .from('#panel3 .infer', 0.5, {x: '100%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel3 #outputtc', 0.5, {x: '-100%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel3 h3', triggerHook:.7})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel4 h2"),1,{opacity:0, scale:3}))
    .add(TweenMax.from(("#panel4 .types"),1,{opacity:0, scale:0}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel4 .pricepoint', triggerHook:.9})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel4 p"),1,{opacity:0, scale:1.5}))
    .from('#panel4 .pricepoint', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel4 .pricepoint', triggerHook:.4})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);
    
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie0", triggerHook:.8})  
.setClassToggle('#panel4 .pricepie0','pricepie0_2')
scene.reverse(false)
.addTo(controller);  
            
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie1", triggerHook:.7})  
.setClassToggle('#panel4 .pricepie1','pricepie1_2')
scene.reverse(false)
.addTo(controller);  
        
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie2", triggerHook:.65})  
.setClassToggle('#panel4 .pricepie2','pricepie2_2')
scene.reverse(false)
.addTo(controller);  
            
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie3", triggerHook:.6})  
.setClassToggle('#panel4 .pricepie3','pricepie3_2')
scene.reverse(false)
.addTo(controller);  
                
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie4", triggerHook:.55})  
.setClassToggle('#panel4 .pricepie4','pricepie4_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie5", triggerHook:.5})  
.setClassToggle('#panel4 .pricepie5','pricepie5_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie6", triggerHook:.45})  
.setClassToggle('#panel4 .pricepie6','pricepie6_2')
scene.reverse(false)
.addTo(controller);  
                    
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie7", triggerHook:.4})  
.setClassToggle('#panel4 .pricepie7','pricepie7_2')
scene.reverse(false)
.addTo(controller);    
    
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .pricepie8", triggerHook:.35})  
.setClassToggle('#panel4 .pricepie8','pricepie8_2')
scene.reverse(false)
.addTo(controller);  
        
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .button0", triggerHook:.7})  
.setClassToggle('#panel4 .button0','button0_2')
scene.reverse(false)
.addTo(controller);  

var tween = TweenMax.to(".button2", 1, {opacity:1, scale: 1});
var scene = new ScrollMagic.Scene({triggerElement:"#panel4 .button2", triggerHook:.7})  
.setTween(tween)
.addTo(controller);

var timeline = new TimelineMax()
    .from('#panel4 #imaget1', 1, {x: '-100%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel4 #imaget1', triggerHook:.5})
.setTween(timeline)
scene.reverse(false)
.addTo(controller); 
    
var timeline = new TimelineMax()
    .from('#panel4 .infer', 0.5, {x: '100%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel4 #outputtt', 0.5, {x: '-100%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel4 h3', triggerHook:.7})
.setTween(timeline)
scene.reverse(false)    
.addTo(controller);
    
});
    
/*.addIndicators({
			name: 'fade scene',
			colorTrigger: 'black',
			colorStart: '#75C695',
			colorEnd: 'pink'
		}) 
*/
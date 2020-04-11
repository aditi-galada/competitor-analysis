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
    
//REPEAT NEXT 3 PARAS. CHANGE PANEL2, leeimage1,2,3
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel2 h2"),1,{opacity:0, scale:3}))
    .from('#panel2 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel2 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel2', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel2 .leeimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel2 .leeimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel2 .leeimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel2 .leeimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel2 .leeimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel3 h2"),1,{opacity:0, scale:3}))
    .from('#panel3 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel3 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel3', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel3 .levisimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel3 .levisimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel3 .levisimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel3 .levisimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel3 .levisimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel4 h2"),1,{opacity:0, scale:3}))
    .from('#panel4 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel4 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel4', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel4 .pepejeansimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel4 .pepejeansimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel4 .pepejeansimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel4 .pepejeansimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel4 .pepejeansimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel5 h2"),1,{opacity:0, scale:3}))
    .from('#panel5 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel5 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel5', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel5 .jackandjonesimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel5 .jackandjonesimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel5 .jackandjonesimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel5 .jackandjonesimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel5 .jackandjonesimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);    
    
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel6 h2"),1,{opacity:0, scale:3}))
    .from('#panel6 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel6 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel6', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel6 .uspoloimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel6 .uspoloimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel6 .uspoloimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel6 .uspoloimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel6 .uspoloimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);      
    
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel7 h2"),1,{opacity:0, scale:3}))
    .from('#panel7 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel7 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel7', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel7 .ucbimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel7 .ucbimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel7 .ucbimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel7 .ucbimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel7 .ucbimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);    
    
    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel8 h2"),1,{opacity:0, scale:3}))
    .from('#panel8 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel8 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel8', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel8 .AmericanEagleimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel8 .AmericanEagleimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel8 .AmericanEagleimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel8 .AmericanEagleimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel8 .AmericanEagleimage3', triggerHook:.2})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);  

    
var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel9 h2"),1,{opacity:0, scale:3}))
    .from('#panel9 h3', 1, {x: '-150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
    .from('#panel9 p', 1, {x: '150%', delay:0.5, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel9', triggerHook:.3})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);
    
var timeline = new TimelineMax()
    .from('#panel9 .celioimage1', 1, {x: '-150%', delay:0, opacity:0, ease:Power0.easeOut},0)
    .from('#panel9 .celioimage2', 1, {x: '150%', delay:0, opacity:0, ease:Power0.easeOut},0)
var scene= new ScrollMagic.Scene({triggerElement:'#panel9 .celioimage1', triggerHook:.45})
.setTween(timeline)
scene.reverse(false)
.addTo(controller);

var timeline = new TimelineMax()
    .add(TweenMax.from(("#panel9 .celioimage3"),1,{opacity:0, scale:1.25}))
var scene= new ScrollMagic.Scene({triggerElement:'#panel9 .celioimage3', triggerHook:.2})
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
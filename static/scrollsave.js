var scrollsave=(function(){
	var position=0;
	var width=0;

	var scrolled = function(){
		position=document.documentElement.scrollTop || document.body.scrollTop;
		width =document.body.clientWidth;
	}
	
	var resized = function(){
		if(width!=document.body.clientWidth){
			window.scroll( 0, position*document.body.clientWidth/width); 
			position=document.documentElement.scrollTop || document.body.scrollTop;
			width=document.body.clientWidth;
		}	
	}
	
	return {
		init:function(){
			window.addEventListener("scroll", scrolled);
			window.addEventListener("resize", resized);
		}
	};
})();
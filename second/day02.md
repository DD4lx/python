1. Javascript中的事件处理
- 在标签上使用onXXX属性来进行事件绑定
- 通过代码获取标签绑定onXXX属性 
- 通过代码获取标签然后使用addEventListener()绑定事件 
- 使用removeEventListener()反绑定事件
- 这里有浏览器兼容性问题 对于低版本IE要使用attchEvent()/detachEvent();
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<button id="btn1" <!--onclick="sayHello()"-->>按钮一</button>
		<script src="js/mylib.js"></script>
		<script>
			var btn1 = document.getElementById('btn1');
			// 绑定事件的回调函数（callback function）
			// 你知道事件发生的时候要做什么，但不知道事件什么时候发生
			// 这个时候都是通过绑定回调函数将来由其他地方来调用。
			bind(btn1,"click",sayHello);
			bind(btn1,"click",sayGoodBye);
			bind(btn1,"click",function(){
				unbind(btn1,"click",sayGoodBye);
			});
			
//			if(btn1.addEventListener){
//				btn1.addEventListener("click",sayHello);
//				btn1.addEventListener("click",sayGoodBye);
//				btn1.addEventListener("click",function(){
//					btn1.removeEventListener("click",sayHello);
//					btn1.removeEventListener("click",sayGoodBye);
//					
//				});
//			}else{
//				btn1.attachEvent("onclick",sayHello);
//				btn1.attachEvent("onclick",sayGoodBye);
//				btn1.attachEvent("onclick",function(){
//					btn1.detachEvent("onclick",sayHello);
//					btn1.detachEvent("onclick",sayGoodBye);
//				});
//			}
//			btn1.onclick = sayHello();
//			btn1.onclick = sayHello;
//			btn1.onclick = sayGoodBye;

			
			
			
			
			function sayHello(){
				window.alert("你好呀！");
			}
			
			function sayGoodBye(){
				window.alert("下次再见")
			}
		</script>
		
	</body>
</html>
```
2.事件回调函数和事件对象
- 绑定事件监听器的函数都需要传入事件的回调函数
- 程序员知道发生的时候需要做什么样的处理但是不知道事情什么时候发生
- 所以要传入一个函数在将来发生事件的时候由系统进行调用；这种函数就称为回调函数
- 回调函数的第一个参数代表事件对象（封装了和事件相关的所有信息）对于低版本的IE可以通过window.event来获取事件对象
- 事件对象的属性和方法：
- - target/srcElement - 事件源（引发事件的标签）
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<div id="buttons">
			<button>Button1</button>
			<button>Button2</button>
			<button>Button3</button>
			<button>Button4</button>
			<button>Button5</button>
		</div>
		
		<script src="js/mylib.js"></script>
		<script>
			var buttons = document.getElementById('buttons').children;
			// var buttons = document.querySelectorAll("#buttons>button");
			for(var i = 0; i < buttons.length; i += 1){
				// 如果希望在事件回调函数中获得事件源（引发事件的标签）
				// 应该通过事件对象的target属性来获取事件源
				bind(buttons[i], "click", function(evt){
					evt = evt || window.event;
					// ie中是srcElement
					evt.target = evt.target || evt.srcElement;
					evt.target.innerHTML = "哦也";			
				})
			}
		</script>
	</body>
</html>
```
- - preventDefault()/returnValue=false - 阻止事件的默认行为
- - 处理事件有两种顺序：事件冒泡（默认，从内向外）/事件捕获（从外向内）
- - 如果要阻止事件的传播行为（例如阻止事件冒泡）可以使用stopPropagation()/cancelBubble=true
实例1
```
<!--实例1-->
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<a id="about" href="http://www.baidu.com">关于</a>
		<script src="js/mylib.js"></script>
		<script>
			var a = document.getElementById('about');
			bind(a, "click", function(evt){
				evt = evt || window.event;
				if(evt.preventDefault){
					// 阻止事件的默认行为；
					evt.preventDefault();
				}else{
					evt.returnValue = false;
				}
				
				
				
				console.log('hello,world!')
			});
		</script>
		
	</body>
</html>

```
实例2
```
<!DOCTYPE html>
<html>
	
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			*{
				margin: 0;
				padding: 0;
				
			}
			#div1{
				width: 400px;
				height: 400px;
				background-color: red;
				
			}
			#div1 #div2{
				width: 300px;
				height: 300px;
				background-color: green;
				
				
			}
			#div1 #div2 #div3{
				width: 200px;
				height: 200px;
				background-color: blue;
			}
			#div2,#div3{
				position: relative;
				left: 50px;
				top: 50px;
			}
		</style>
	</head>
	<body>
		<div id="div1">
			<div id="div2">
				<div id="div3">
			
				</div>
			
			</div>
		
		</div>
		<script src="js/mylib.js"></script>
		<script>
			var one = document.getElementById('div1');
			bind(one, "click", function(){
				window.alert("i am one");
			});
			var two = document.getElementById('div2');
			bind(two, "click", function(){
				window.alert("i am two");
			});
			var three = document.getElementById('div3');
			bind(three, "click", function(evt){
				evt = evt || window.event;
				if(evt.stopPropagation){
					evt.stopPropagation();
				}else{
					evt.cancelBubble = true;
				}
				window.alert("i am three");
				
			});
		</script>
		
	</body>
</html>

```
>猜数字游戏
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<input id="input" type="text" placeholder="请输入你猜的数字"/>
		<button id="sure">确定</button>
		<p id="result"></p>
		<script src="js/mylib.js"></script>
		<script>
			var number = parseInt(Math.random()*100+1);
			console.log(number);
			var value = document.getElementById('input');
			var result = document.getElementById('result');
			var btn1 = document.getElementById('sure');
			var count = 0;
			bind(btn1,"click", guess);
			bind(value,"keydown",function(evt){
				evt = evt || window.event;
				
				if (evt.keyCode == 13 || evt.which == 13){
					guess();
				}
			});
			function guess(){
				
				if (number == parseInt(value.value)){
					count += 1;
					result.textContent = "恭喜你，猜对了！一共猜了" + count +"次";
					btn1.disabled = true;
				}else if(number < parseInt(value.value)){
					count += 1;
					result.textContent = "可惜，太大了！"
					
				}else if(number > parseInt(value.value)){
					count += 1;
					result.textContent = "可惜，太小了！"
					
				}else{
					count += 1;
					result.textContent = "数据不正确！"
				}
				value.value = "";
				value.focus();
			}
			
		</script>
	</body>
</html>

```
>图片轮播作业
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			* {
				margin: 0;
				padding: 0;
			}
			#adv {
				width: 940px;
				margin: 0 auto;
			}
			#adv ul {
				width: 120px;
				height: 30px;
				margin: 0 auto;
				position: relative;
				top: -30px;
			}
			#adv li {
				width: 30px;
				height: 30px;
				list-style: none;
				float: left;
				color: #ccc;
				cursor: pointer;
			}
			#adv li:first-child {
				color: lightseagreen;
			}
		</style>
	</head>
	<body>
		<div id="adv">
			<img src="img/slide-1.jpg" alt="">
			<ul>
				<li class="dot">●</li>
				<li class="dot">●</li>
				<li class="dot">●</li>
				<li class="dot">●</li>
			</ul>
		</div>
		<script src="js/mylib.js"></script>
		<script>
			function changeImage() {
				index += 1;
				index %= 4;
				var counter = 20;
				var opacity = 1.0;
				setTimeout(function() {
					if (counter > 0) {
						counter -= 1;
						opacity -= 0.05;
						// 通过image标签的style属性修改opacity样式调整透明度
						img.style.opacity = opacity;
						setTimeout(arguments.callee, 30);
					} else {
						img.src = "img/slide-" + (index + 1) + ".jpg";
						resetDotColor();
						dotItems[index].style.color = "lightseagreen";
						counter = 0;
						opacity = 0;
						setTimeout(function() {
							if (counter < 20) {
								counter += 1;
								opacity += 0.05;
								img.style.opacity = opacity;
								setTimeout(arguments.callee, 20);
							}
						}, 20);
					}
				}, 30);	
			}
			function resetDotColor() {
				for (var i = 0; i < dotItems.length; i += 1) {
					dotItems[i].style.color = "white";
				}
			}
			var index = 0;
			var advDiv = document.getElementById("adv");
			var img = document.querySelector("#adv>img");
			var dotItems = document.querySelectorAll("#adv li");
			for (var i = 0; i < dotItems.length; i += 1) {
				dotItems[i].index = i;
				bind(dotItems[i], "click", function(evt) {
					evt = evt || window.event;
					evt.target = evt.target || evt.srcElement;
					index = evt.target.index;
					img.src = "img/slide-" + (index + 1) + ".jpg";
					resetDotColor();
					evt.target.style.color = "lightseagreen";
				});
			}
			var timerId = setInterval(changeImage, 3000);
			bind(advDiv, "mouseover", function() {
				clearInterval(timerId);
			});
			bind(advDiv, "mouseout", function() {
				timerId = setInterval(changeImage, 3000);
			});
		</script>
	</body>
</html>

```
>图片展示作业
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		
	</head>
	<body>
		<div>
			<img id="big" src="img/hello.jpg" alt="" />
		</div>
		<div id="smallimg">
			<img id="small1" src="img/thumb-1.jpg" alt="" />
			<img id="small2" src="img/thumb-2.jpg" alt="" />
			<img id="small3" src="img/thumb-3.jpg" alt="" />
		</div>
		
		<script src="js/mylib.js"></script>
		<script>
			var big = document.getElementById('big');
			var img = document.getElementById('smallimg');
			var imgName = '';
			bind(img, "mouseover", function(evt){
				evt = evt || window.event;
				if(evt.target.id == "small1"){
					imgName = "hello";
				}else if(evt.target.id == "small2"){
					imgName = "goodbye";
					
				}else{
					imgName = "oneshit";
				}
				big.src = "img/" + imgName + ".jpg";
			});
		</script>
		
	</body>
</html>

```
>点击图片优先级最高
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			#one {
				position: fixed;
				width: 300px;
				height: 300px;
				left: 50px;
				top: 50px;
				background-color: lightgreen;
			}
			#two {
				position: fixed;
				width: 200px;
				height: 200px;
				right: 50px;
				bottom: 50px;
				background-color: lightpink;
			}
			#three {
				position: fixed;
				width: 250px;
				height: 250px;
				left: 50px;
				bottom: 50px;
				background-color: darkgrey;
			}
		</style>
	</head>
	<body>
		<div id="one"></div>
		<div id="two"></div>
		<div id="three"></div>
		<script src="js/mylib.js"></script>
		<script>
			var draggables = [];
			
			function makeDraggable(div) {
				draggables.push(div);
				div.isMouseDown = false;
				div.originX = 0;
				div.originY = 0;
				div.oldX = 0;
				div.oldY = 0;
				div.start = function(evt) {
					for (var i = 0; i < draggables.length; i += 1) {
						draggables[i].style.zIndex = 0;
					}
					this.style.zIndex = 10;
					this.isMouseDown = true;
					var currentStyle = document.defaultView.getComputedStyle(this);
					this.originX = parseInt(currentStyle.left);
					this.originY = parseInt(currentStyle.top);
					this.oldX = evt.pageX;
					this.oldY = evt.pageY;
				};
				div.move = function(evt) {
					if (this.isMouseDown) {
						var dx = evt.pageX - this.oldX;
						var dy = evt.pageY - this.oldY;
						this.style.left = this.originX + dx + "px";
						this.style.top = this.originY + dy + "px";
					}
				};
				div.stop = function() {
					this.isMouseDown = false;
				};
				bind(div, "mousedown", div.start);
				bind(div, "mousemove", div.move);
				bind(div, "mouseup", div.stop);
				bind(div, "mouseout", div.stop);
			}
			
			makeDraggable($("one"));
			makeDraggable($("two"));
			makeDraggable($("three"));
		</script>
	</body>
</html>

```

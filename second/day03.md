>广告位招租实例
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			#adv{
				background-color: blue;
				position: fixed;
				top: 10px;
				right: 10px;
				width: 100px;
				height: 200px;
			}
			#close{
				float: right;
			}
		</style>
		
	</head>
	<body>
		<div id="adv">
			广告位招租
			<button id="close">关闭</button>
		</div>
		
		<script src="js/mylib.js"></script>
		<script>
			var closeBtn = document.getElementById('close');
			bind(closeBtn, "click", function(){
				//children--子节点
				//parentNode--父节点
				
				//previousSibling/nextSibling--兄弟节点
				// 只能写样式，不能读样式
				//closeBtn.parentNode.style.display = "none";//消失
				//closeBtn.parentNode.style.visibility = "hidden";//隐藏	
				var adv = closeBtn.parentNode;
				//只能读样式，不能写样式
				var currentStyle = adv.currentStyle ? adv.currentStyle :
									document.defaultView.getComputedStyle(adv);
				alert(currentStyle.width);
				alert(currentStyle.height);
				alert(currentStyle.backgroundColor);
				
				var width = parseInt(currentStyle.width) + 50;
				var height = parseInt(currentStyle.height) + 50;
				adv.style.width = width + "px";
				adv.style.height = height + "px";
				
			});
		</script>
		
	</body>
</html>

```
>网页中拖动标签实例
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			
			#drag{
				width: 80px;
				height: 80px;
				background-color: blue;
				position: fixed;
				left: 50px;
				top: 50px;
				
			}
		</style>
	</head>
	<body>
		<div id="drag">
			
		</div>
		
		<script src="js/mylib.js">
			
		</script>
		<script>
			
			var drag = document.getElementById("drag");
			var isMouseDown = false;
			var originX = 0, originY = 0;
			var oldX = 0, oldY = 0;
			bind(drag,"mousedown",function(evt){
				isMouseDown = true;
				var currentStyle = document.defaultView.getComputedStyle(drag);
				originX = parseInt(currentStyle.left);
				originY = parseInt(currentStyle.top);
				oldX = evt.pageX;
				oldY = evt.pageY;
			});
			bind(drag,"mousemove",function(evt){
				if(isMouseDown){
					var dx = evt.pageX - oldX;
					var dy = evt.pageY - oldY;
					drag.style.left = originX + dx + "px";
					drag.style.top = originY + dy + "px";
				}
				
			});
			bind(drag,"mouseup",function(){
				isMouseDown = false;
			});
			bind(drag,"mouseout",function(){
				isMouseDown = false;
			});
			
		</script>
	</body>
</html>

```
>添加删除水平列表实例
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
			#container {
				margin: 20px 50px;
			}
			#fruits li {
				list-style: none;
				width: 200px;
				height: 50px;
				font-size: 20px;
				line-height: 50px;
				background-color: cadetblue;
				color: white;
				text-align: center;
				margin: 2px 0;
			}
			#fruits>li>a {
				float: right;
				text-decoration: none;
				color: white;
				position: relative;
				right: 5px;
			}
			#fruits~input {
				border: none;
				outline: none;
				font-size: 18px;
			}
			#fruits~input[type=text] {
				border-bottom: 1px solid darkgray;
				width: 200px;
				height: 50px;
				text-align: center;
			}
			#fruits~input[type=button] {
				width: 80px;
				height: 30px;
				background-color: coral;
				color: white;
				vertical-align: bottom;
				cursor: pointer;
			}
		</style>
	</head>
	<body>
		<div id="container">
			<ul id="fruits">
				<li>苹果<a href="javascipt:void(0)">×</a></li>
				<li>香蕉<a href="javascipt:void(0)">×</a></li>
				<li>火龙果<a href="javascipt:void(0)">×</a></li>
				<li>西瓜<a href="javascipt:void(0)">×</a></li>
			</ul>
			<input type="text" name="fruit">
			<input id="ok" type="button" value="确定">
		</div>
		
		<script src="js/mylib.js"></script>
		<script>
			var deAchors = document.querySelectorAll("#fruits a");
			for (var i = 0; i < deAchors.length; i += 1){
				bind(deAchors[i],"click",deleteItems)
			}
			function deleteItems(evt){
				evt = evt || window.event;
				evt.target = evt.target ||evt.srcElement;
				var li = evt.target.parentNode;
				li.parentNode.removeChild(li);
			}
			
			var okBtn = document.getElementById('ok');
			var input = document.querySelector('#container>input[type=text]')
			var fruitsUl = document.getElementById('fruits');
			bind(okBtn,"click",function(){
				var fruitName = input.value.trim();
				if (fruitName.length > 0){
					var li = document.createElement("li");
					var a = document.createElement("a");
					li.innerHTML = fruitName;
					a.innerHTML = "×";
					a.href = "javascript:void(0)";
					bind(a, "click", deleteItems);
					li.appendChild(a);
					// fruitsUl.appendChild(li);
					// 另外一种
					fruitsUl.insertBefore(li,fruitsUl.firstChild);
					
				}
			});
		</script>
		
	</body>
</html>


```
>产生随机颜色的方块，而且可以控制其闪烁实例
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			#parent{
				width: 800px;
				height: 400px;
				margin: 0 auto;
				border: 1px solid black;
				/*溢出属性：默认是visible、hidden、scorll*/
				overflow: hidden;
			}
			#add,#randomColor{
				width: 60px;
				background-color: orange;
			}
			#btn{
				text-align: center;
			}
			.small{
				width: 80px;
				height: 80px;
				float: left;
			}
		</style>
	</head>
	<body>
		<!--<script>
			在HTML之前写js需要窗口加载完成后，再执行。如下：
			bind(window,'load',function(){});
		</script>-->
		<div id="parent">
			
		</div>
		<div id="btn">
		<button id="add">添加</button>
		<button id="randomColor">闪烁</button>
		</div>
		
		<script src="js/mylib.js"></script>
		<script>
			var add = document.getElementById('add');
			var randomBtn = document.getElementById('randomColor');
			var parent = document.getElementById('parent');
			var count = 1;
			bind(add,"click",function(){
				if(count <= 50){
					var div = document.createElement("div");
	//				div.style.width = "80px";
	//				div.style.height = "80px";
	//				div.style.float = "left";
					div.className = "small";
					div.style.backgroundColor = randomColor();
					parent.appendChild(div);
					count += 1;
				}
				
			});
			function randomColor(){
				var red = parseInt(Math.random()*256);
				var green = parseInt(Math.random()*256);
				var blue = parseInt(Math.random()*256);
				return "rgb("+red+","+green+","+blue+")";
			}
			var isFlashing = false;
			var timer = 0;
			bind(randomBtn,"click",function(evt){
				if (isFlashing){
					clearInterval(timer);
				}else{
					timer = setInterval(changeColor, 50);
				}
				randomBtn.innerHTML = isFlashing?"闪烁":"暂停";
				isFlashing = !isFlashing;
			});
			function changeColor(){
				for (var i = 0; i < parent.children.length; i += 1){
					parent.children[i].style.backgroundColor = randomColor();
				}
			}
		</script>
		
	</body>
</html>

```
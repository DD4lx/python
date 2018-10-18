## 学习使用jquery
>要使用jQuery就必须先引入jQuery
1. 在网上下载对应版本的jQuery文件
2. 使用自己项目中的jQuery.min.js
3. 也可以使用cdn服务器上的jQuery文件
4. 使用jQuery的语句- window.jQuery属性  或者-- $
```
<script src="js/jquery.min.js"></script>
```
>jQuery对象的本质是一个伪数组
- 有length属性
- 可以通过下标获取数据
>$函数的四种用法：
1. $函数的参数是一个函数 - 传入的函数是页面加载完成之后要执行的回调函数；
2. $函数的参数是选择器字符串 - 获取页面上的标签而且转成jQuery对象；
- 为什么要获取jQuery对象 -- 因为jQuery对象有更多的封装好的方法可以调用；
- - 绑定、反绑定事件：on()/off()/one();
- - 获取、修改标签内容：text()/html();
- - 获取、修改标签属性：attr(name,value);
- - 添加子节点：append()、prepend();
- - 删除、清空节点：remove()/empty();
- - 获取父节点：parent() ;
- - 获取子节点：children();
- - 获取兄弟节点：prev()/next();
- - 修改样式表：css()读("color")改("color","red")改多个({'color':'red','font-size':'18px'})
3. $函数的参数是标签字符串 -  创建标签并且返回对应jQuery对象；
4. $函数的参数是原生js对象 - 将原生js对象转换成jQuery对象；
>下面将使用jQuery重写之前的页面
>5秒钟跳转页面实例
```
<body>
		<h2><span id="counter">5</span>秒钟以后自动跳转到百度...</h2>
		<script src="js/jquery.min.js"></script>
		<script>
			var index = $("#counter").text();
			function delay(){
				if (index > 0){
				index -= 1;
				setTimeout(function(){
					$("#counter").text(index);
				},1000);
				}else{
					location.href = "http://www.baidu.com";
				}
			}
			
			setInterval(delay,1000);
		</script>
	</body>
```
>实现文字广告轮播显示
```
<body>
		<div id="title">
			<h1 id="content">欢迎来到成都玩耍&nbsp;&nbsp;&nbsp;！</h1>
		</div>
		<div id="time">
			
		</div>
		
		<script src="js/jquery.min.js"></script>
		<script>
			setInterval(function(){
				$("#content").text($("#content").text().substring(1) + $("#content").text().charAt(0)); 
			},1000);
			setInterval(function(){
				$("#time").text(Date);
			},1000);
		</script>
		
		
		
	</body>
```
>实现点击按钮后，按钮的文字发生改变
```
<body>
		<div id="buttons">
			<button>Button1</button>
			<button>Button2</button>
			<button>Button3</button>
			<button>Button4</button>
			<button>Button5</button>
		</div>
		
		<script src="js/jquery.min.js"></script>
		<script>
			$("#buttons button").on("click",function(){
				for(var i = 0; i < $("#buttons button").length; i += 1){
					this.textContent = "哦也";
				}
			});
		</script>
	</body>
```
>使用jQuery重写水果列表实例
```
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
		
		
		<script src="js/jquery.min.js"></script>
		<script>
		    $(function(){
				function deleteItem(evt){
					$(evt.target).parent().remove();
				}
				$("#fruits a").on("click",deleteItem);
				$("#ok").on("click",function(){
					var fruitName = $("#container input[type=text]").val().trim();
					if(fruitName.length > 0){
						$("#fruits").append(
							$("<li>").text(fruitName).append(
								$("<a>").text("×").attr("href", "javascript:void(0)")
								.on("click",deleteItem)
							)
						);
					}
				});
			});
		</script>
</body>
```
>JSON = JavaScipt Object Natation
>JSON 是JavaScript中创建对象的字面量语法；
>JSON被广泛的应用于数据的存储和交换；
实例：
```
<body>
		<script>
			
			function Student(name, age){
				this.name = name;
				this.age = age;
//				this.study = function(courseName){
//					alert(this.name + "正在学习" +courseName);
//				};
			}
			Student.prototype.study = function(courseName){
				alert(this.name + "正在学习" +courseName);
			};
			Student.sayHello = function(){
				alert("你好");
			};
			var obj = new Student('小李',21);
			obj.study("js");
			Student.sayHello();
			
			
			
			
			
			
			// JSON = JavaScript Object Notation
			// JSON 是JavaScript中创建对象的字面量语法；
			// JSON被广泛的应用于数据的存储和交换
			/*
			var obj = {
				"name": "小李",
				"age": 8,
				"study": function(courseName){
				alert(this.name + "正在学习" + courseName);
				},
				"watchAv": function(){
					if (this.age < 18){
					alert(this.name + "建议你看动画片");
					}else{
					alert(this.name + "正在看");
					}
				}	
			};
			obj.study("java");
			obj.watchAv();
			*/
//			var obj = new Object();
//			obj.name = "小李";
//			obj.age = "20";
//			obj.study = function(courseName){
//				alert(this.name + "正在学习" + courseName);
//			};
//			obj.watchAv = function(){
//				if (this.age < 18){
//					alert(this.name + "建议你看动画片");
//				}else{
//					alert(this.name + "正在看");
//				}
//			};
//			obj.study("python");
//			obj.watchAv();
		</script>
	</body>
```
>产生随机颜色的模块，并且可以随机更改颜色
```
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
		
		<script src="js/jquery.min.js"></script>
		<script>
			$(function(){
				$("#add").on("click",function(){
					$("#parent").append($("<div>").addClass("small").css("background-color",randomColor()))
				});
				function randomColor(){
					var red = parseInt(Math.random()*256);
					var green = parseInt(Math.random()*256);
					var blue = parseInt(Math.random()*256);
					return "rgb(" + red + "," + green + "," + blue + ")";
				}
				$("#randomColor").on("click",function(){
					setInterval(function(){
						$("#parent div").each(function(){
							$(this).css("background-color",randomColor());
						});
					},200);
				});
				
				
			});
			
		</script>
	</body>
```
>表格的基本操作
```
<head>
		<meta charset="UTF-8">
		<title></title>
		<style>
			#data {
				border-collapse: collapse;
			}
			#data td, #data th {
				width: 120px;
				height: 40px;
				text-align: center;
				border: 1px solid black;
			}
			#buttons {
				margin: 10px 0;
			}
		</style>
	</head>
	<body>
		<table id="data">
			<caption>数据统计表</caption>
			<tr>
				<th>姓名</th>
				<th>年龄</th>
				<th>性别</th>
				<th>身高</th>
				<th>体重</th>
			</tr>
			<tr>
				<td>Item1</td>
				<td>Item2</td>
				<td>Item3</td>
				<td>Item4</td>
				<td>Item5</td>
			</tr>
			<tr>
				<td>Item1</td>
				<td>Item2</td>
				<td>Item3</td>
				<td>Item4</td>
				<td>Item5</td>
			</tr>
			<tr>
				<td>Item1</td>
				<td>Item2</td>
				<td>Item3</td>
				<td>Item4</td>
				<td>Item5</td>
			</tr>
			<tr>
				<td>Item1</td>
				<td>Item2</td>
				<td>Item3</td>
				<td>Item4</td>
				<td>Item5</td>
			</tr>
			<tr>
				<td>Item1</td>
				<td>Item2</td>
				<td><a>Item3</a></td>
				<td>Item4</td>
				<td>Item5</td>
			</tr>
			<tr>
				<td>Item1</td>
				<td>Item2</td>
				<td>Item3</td>
				<td>Item4</td>
				<td><a>Item5</a></td>
			</tr>
		</table>
		<div id="buttons">
			<button id="pretty">美化表格</button>
			<button id="clear">清除数据</button>
			<button id="remove">删单元格</button>
			<button id="hide">隐藏表格</button>
		</div>
		
		<script src="js/jquery.min.js"></script>
		<script>
			$(function(){
				$("#pretty").on("click",function(){
					$("#data tr:gt(0):odd").css("background-color", "lightcyan");
					$("#data tr:gt(0):even").css("background-color", "lightpink");
				});
				
				$("#clear").on("click",function(){
					$("#data tr:gt(0) td").empty();
				});
				
				$("#remove").on("click",function(){
					$("#data tr:gt(0):last-child").remove();
				});
				
				$("#hide").on("click",function(){
					if (this.isHidden){
						$("#data").show();
						this.isHidden = false;
						$(this).text("隐藏表格");
					}else{
						$("#data").hide();
						this.isHidden = true;
						$(this).text("显示表格");
					}
					
				});
			});
		</script>
		
		
	</body>
```
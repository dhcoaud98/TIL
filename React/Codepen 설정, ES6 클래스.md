## Codepen 설정, ES6 클래스, JSX, Props, State

* 컴포넌트 = 자바스크립트 클래스
  * 리액트 컴포넌트 클래스를 상속
* `render` 는 컴포넌트가 어떻게 렌더되는지 정의함.

* JSX : 자바스크립트 코드에서 HTML 코드 형식을 작성할 수 있다. (react_jsx)



### **기본 문법** 이해하기

```html
<!-- HTML -->
<div id="root"></div>
```

```javascript
// js
class Codelab extends React.Component {
  render() {
    return (
      // JSX
      <div>Codelab</div>
    );
  }
}

class App extends React.Component {
  render() {
    return (
      <Codelab/>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById('root'));
```

1. `Codelab` 이라는 컴포넌트를 만든다. 이때 이 컴포넌트는 React.component를 상속 받는다. 
2. 이를 render 해주어야 하는데, render는 컴포넌트가 어떻게 렌더되는지 정의한다는 뜻이다.
3. JSX 문법을 지원하기 때문에 js 코드 안에서 HTML을 작성할 수 있다. 이때 `return()` 의 형식으로 사용한다. 
4. 두 번째 컴포넌트인 App 컴포넌트를 만든다. 이 역시 React.component를 상속 받는다. 
5. 여기에서는 `<Codelab/>` 컴포넌트를 보여준다.
6. HTML 파일에서 `root` 를 id로 가지는 div 태그를 만든다. 
7. js 파일에서 ReactDOM.render를 통해 우리가 만든 코드를 렌더한다. 
8. 인자로는 `<App/>`과 `document.getElementById('root')` 를 가진다.



### JSX 특징

1. 모든 JSX 형태는 꼭 component element 안에 포함시켜야 한다.

   ```javascript
   /* 에러 */
   
   render() {
     return (
       <h1></h1>
       <h2></h2>
     )
   }
   
   /* 정답 */
   
   render() {
     return (
       <div>
   	  <h1></h1>
         <h2></h2>
       </div>
     )
   }
   ```

2. JSX 안에서 JavaScript를 표현하는 방법은 **{}**로 **wrapping** 하는 것이다.

   ```javascript
   render() {
     let text="Hello React";
     return (
       <div>{text}</div>
     )
   }
   ```

3. JSX 안에서 style을 설정할 때는, string 형식은 사용하지 않고, key가 camelCase인 객체가 사용된다.

   ```javascript
   render() {
     let style = {
       color: 'aqua',
       backgroundColor: 'blank'
     };  
     
     return (
       <div style={style}>React Codelab</div>
     )
   }
   ```

4. JSX 안에서 class를 설정할 때는 class=""가 아닌 className=""를 사용한다. 

   ```javascript
   render() {
     return(
       <div className="box">React Codelab</div>
     )
   }
   ```

5. 주석은 { /* .. */ }로 작성한다. 주석은 container element 안에 작성되어야 한다. 

   ```javascript
   render() {
     return (
     	<div>
         {/*This is How You Comment*/}
         {/*Multi-line
         	   Testing*/}
   		React Codelab
       </div>
     )
   }
   ```

   
## Codepen 설정, ES6 클래스, JSX, Props, State, 컴포넌트 매핑

* 컴포넌트 = 자바스크립트 클래스
  * 리액트 컴포넌트 클래스를 상속
* `render` 는 컴포넌트가 어떻게 렌더되는지 정의함.

* JSX : 자바스크립트 코드에서 HTML 코드 형식을 작성할 수 있다. (react_jsx)



### 1. **기본 문법** 이해하기

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



### 2. JSX 특징

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

   

### 3. props

* 컴포넌트 내부의 Immutable Data
* JSX 내부에 { this.props.propsName }
* 컴포넌트를 사용 할 떄, <> 괄호 안에 propsName="value"
* this.props.children은 기본적으로 갖고 있는 props로서, <Cpnt>여기에 있는 값이 들어간다.</Cpnt>



**props의 기본 값 설정**

```javascript
class App extends React.Component {
  render() {
    return (
      <div>{this.props.value}</div>
    );
  }
};
 
/* component.defalutProps */
App.defaultProps = {
  value: 0   
}
```

**Type 검중**

```javascript
class App extends React.component {
  render() {
    return (
      <div>
        {this.props.value}
        {this.props.secondValue}
    	{this.props.thirdValue}
      </div>
    );
  }
};

/* component.propTypes */
App.propTypes = {
  value: React.propTypes.string,
  secondValue: React.PropType.number,
  thirdValue: React.PropTypes.any.isRequired
}
```





### 4. state

* 유동적인 데이터
* JSX 내부에 {this.state.stateName}
* 초기값 설정이 필수, 생성자(constructor)에서 this.state= {} 으로 설정
* 값을 수정 할 때에는 this.setState({ ... }), 렌더링 된 다음엔 this.state = 절대 사용하지 말것

```javascript
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 0
    };
    this.handleClick = this.handleClick.bind(this);
  }
  
  
  handleClick() {
    this.setState({
      value:this.state.value + 1
    })   --- (2)
  }
  render() {
    return (
      <div>
        <h2>{this.state.value}</h2>
        <button onClick={this.handleClick}>Press Me</button>  --- (1)
      </div>
    );
  }
};

class App extends React.Component {
  render () {
    return (
      <Counter/>
    );
  }
};

ReactDOM.render(
  <App></App>, document.getElementById('root')
)
```

* (1)에서 `this.handleClick()` 처럼 **()**를 쓰면 어떻게 될까?
  * 최초 렌더링 이후 handleClick()에 의해 setState가 실행되어 +1 이 되고, setState에 의해 다시 렌더링 되고, 렌더링 되면 handleClick()가 반복된다. 중간에 react가 멈추게 된다.

* (2)에서 this.setState 안에서 value 값을 바꾸는 대신 바로`this.state.value = this.state.value + 1` 을 하게 되면 어떻게 될까?
  * 작동 안됨!



### 5. 컴포넌트 매핑(Component Mapping)

* map() 메소드는 파라미터로 전달 된 함수를 통하여 배열 내의 각 요소를 처리해서 그 결과로 새로운 배열을 생성한다.

* `arr.map(callback, thisArh)`
  * callback 새로운 배열의 요소를 생성하는 함수로서, 다음 세가지 인수를 가진다. 
    * currentValue: 현재 처리되고 있는 요소
    * index: 현재 처리되고 있는 요소의 index 값
    * array 메소드가 불려진 배열
  * thisArg (선택항목)  callback 함수 내부에서 사용 할 this 값을 설정

```javascript
var numbers = [1, 2, 3, 4, 5];

var processed = numbers.map(function(num) {
  return num*num;
});

/* ES6 문법 */
let numbers = [1, 2, 3, 4, 5];

let processed = numbers.map((num) => {  /* 화살표 함수 (콜백 함수를 사용할 떄 많이 사용) */
  return num*num;
})
```

* 배열을 컴포넌트로 매핑 할 수 있음!

```javascript
class ContaxtInfo extends React.Component {
  render() {
    return (
      <div> {this.props.contact.name} {this.props.contact.phone}</div>
    );
  }
};

class Contaxt extends React.Component {
   /* 생성자 데이터  */
   constructor(props) {
     super(props);
     this.state = {
       contactData: [
         {name: 'Abet', phone: '010-0000-0001'},
         {name: 'Betty', phone: '010-0000-0002'},
         {name: 'Charlie', phone: '010-0000-0003'},
         {name: 'David', phone: '010-0000-0004'},
       ]
     }
   }
   render() {
     const mapToComponent = (data) => {
       return data.map((contact, i) => {
         return (<ContaxtInfo contact={contact} key={i}/>)
       })
     }
     return (
      <div>
        {mapToComponent(this.state.contactData)}
      </div>
     );
   }
};

class App extends React.Component {
  render() {
    return (
      <Contaxt/>
    ); 
  }  
};

ReactDOM.render(<App/>, document.getElementById('root'))
```


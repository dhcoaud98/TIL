# Font awesome/bootstrap



```html
<head>
  ...
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <title>Document</title>
</head>
<body>
  <div class="container">
    <span style="font-size: 3em; color: Tomato;">
      <i class="fa-solid fa-heart fa-beat"></i>
    </span>
    <span style="font-size: 3em; color: Tomato;">
      <i class="fas fa-camera"></i>
    </span>
```



```html
<form action='{% url 'articles:likes' article.pk %}' method="POST">
        {% csrf_token %}
        {% if user in article.like_users.all %} 
          {% comment %} <input type='submit' value="좋아요 취소"> {% endcomment %}
          <button type='submit' class="btn btn-link shadow-none">
            <i class="fa-solid fa-heart" style='color: crimson;'></i>
          </button>
        {% else %}
          {% comment %} <input type='submit' value="좋아요"> {% endcomment %}
          <button type='submit' class="btn btn-link shadow-none">
            <i class="fa-solid fa-heart" style='color: black;'></i>
          </button>
        {% endif %} 
      </form>      
...
```


# Ease Css State Manager

### example

#### checbox label trick

```html

<body>
  <h1 handle_state="test">click here</h1>
</body>
```

**compiles to**

```html

<body>

  <input class="ECSM-state" id="ECSM-bool-ID_test" type="checkbox" />

  <label for="ECSM-bool-ID_test">
    <h1>click here</h1>
  </label>
  
</body>
```
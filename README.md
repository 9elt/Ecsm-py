# Ease Css State Manager

### example
checbox label trick

```html
<body>

  <div>
    <h1 handle_state="test">click here</h1>
    <p class="content">hello</p>
  </div>

</body>
```

```css
test:active .content {
  color: #f00
}
```

**compiles to**

```html
<body>

  <input class="ECSM-state" id="ECSM-bool-ID_test" type="checkbox" />

  <div>
    <label for="ECSM-bool-ID_test">
      <h1>click here</h1>
    </label>
    <p class="content">hello</p>
  </div>

</body>
```

```css
#ECSM-bool-ID_test:checked~* .content {
  color: #f00
}
```
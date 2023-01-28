# Ease Css State Manager

### example

#### checbox label trick

```html

<body>

  <div>
    <h1 handle_state="test">click here</h1>
  </div>

</body>
```

**compiles to**

```html

<body>

  <input class="ECSM-state" id="ECSM-bool-ID_test" type="checkbox" />

  <div>

    <label for="ECSM-bool-ID_test">
      <h1>click here</h1>
    </label>

  </div>
</body>
```
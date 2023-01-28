# Ease Css State Manager

## example

### html

<table>

<tr></tr>

<tr>
<td>


```html
<body>

  <div>
    <h1 handle_state="test">click here</h1>
    <p class="content">hello</p>
  </div>

</body>
```

<img width=500/>
</td>

<td>

```html
<body>

  <input
    class="ECSM-state"
    id="ECSM-bool-ID_test"
    type="checkbox"
  />

  <div>
    <label for="ECSM-bool-ID_test">
      <h1>click here</h1>
    </label>
    <p class="content">hello</p>
  </div>

</body>
```

<img width=500/>
</td>
</tr>


</table>

### css

<table>

<tr></tr>

<tr>
<td>


```css
test:active .content {
  color: #f00
}
```

<img width=500/>
</td>

<td>


```css
#ECSM-bool-ID_test:checked~* .content {
  color: #f00
}
```

<img width=500/>
</td>
</tr>


</table>
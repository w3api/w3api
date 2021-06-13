---
title: TextFieldListCell.forListView()
permalink: /Java/TextFieldListCell/forListView/
date: 2021-01-11
key: Java.T.TextFieldListCell
category: Java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextFieldListCell.metodos valor="forListView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Callback<ListView<String>,ListCell<String>> forListView()
static <T> Callback<ListView<T>,ListCell<T>> forListView(StringConverter<T> converter)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}

## Clase Padre
[TextFieldListCell](/Java/TextFieldListCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

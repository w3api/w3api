---
title: TextFieldTreeCell.forTreeView()
permalink: Java/TextFieldTreeCell/forTreeView
date: 2021-01-11
key: JavaJava.T.TextFieldTreeCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextFieldTreeCell.metodos valor="forTreeView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Callback<TreeView<String>,TreeCell<String>> forTreeView()
static <T> Callback<TreeView<T>,TreeCell<T>> forTreeView(StringConverter<T> converter)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}

## Clase Padre
[TextFieldTreeCell](/Java/TextFieldTreeCell/)

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

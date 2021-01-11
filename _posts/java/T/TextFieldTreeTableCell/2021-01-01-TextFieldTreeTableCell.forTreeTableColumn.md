---
title: TextFieldTreeTableCell.forTreeTableColumn()
permalink: Java/TextFieldTreeTableCell/forTreeTableColumn
date: 2021-01-11
key: JavaJava.T.TextFieldTreeTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextFieldTreeTableCell.metodos valor="forTreeTableColumn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S> Callback<TreeTableColumn<S,String>,TreeTableCell<S,String>> forTreeTableColumn()
static <S,T> Callback<TreeTableColumn<S,T>,TreeTableCell<S,T>> forTreeTableColumn(StringConverter<T> converter)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<T> converter" %}

## Clase Padre
[TextFieldTreeTableCell](/Java/TextFieldTreeTableCell/)

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

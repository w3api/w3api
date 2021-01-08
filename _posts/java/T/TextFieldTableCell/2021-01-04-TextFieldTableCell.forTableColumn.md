---
title: TextFieldTableCell.forTableColumn()
permalink: Java/TextFieldTableCell/forTableColumn
date: 2021-01-04
key: JavaJava.T.TextFieldTableCell
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextFieldTableCell.metodos valor="forTableColumn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S> Callback<TableColumn<S,String>,TableCell<S,String>> forTableColumn()
static <S,T> Callback<TableColumn<S,T>,TableCell<S,T>> forTableColumn(StringConverter<T> converter)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<T> converter" %}

## Clase Padre
[TextFieldTableCell](/Java/TextFieldTableCell/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TextFieldTableCell.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

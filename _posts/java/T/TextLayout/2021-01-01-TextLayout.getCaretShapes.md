---
title: TextLayout.getCaretShapes()
permalink: Java/TextLayout/getCaretShapes
date: 2021-01-11
key: JavaJava.T.TextLayout
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.metodos valor="getCaretShapes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Shape[] getCaretShapes(int offset)
public Shape[] getCaretShapes(int offset, Rectangle2D bounds)
public Shape[] getCaretShapes(int offset, Rectangle2D bounds, TextLayout.CaretPolicy policy)
~~~

## Parámetros
* **Rectangle2D bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D bounds" %}
* **TextLayout.CaretPolicy policy**,  {% include w3api/param_description.html metodo=_dato parametro="TextLayout.CaretPolicy policy" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Clase Padre
[TextLayout](/Java/TextLayout/)

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

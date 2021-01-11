---
title: JTextArea.getScrollableUnitIncrement()
permalink: Java/JTextArea/getScrollableUnitIncrement
date: 2021-01-11
key: JavaJava.J.JTextArea
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextArea.metodos valor="getScrollableUnitIncrement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getScrollableUnitIncrement(Rectangle visibleRect, int orientation, int direction)
~~~

## Parámetros
* **Rectangle visibleRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle visibleRect" %}
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}
* **int direction**,  {% include w3api/param_description.html metodo=_dato parametro="int direction" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextArea](/Java/JTextArea/)

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

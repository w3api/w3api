---
title: JTextComponent.getScrollableBlockIncrement()
permalink: /Java/JTextComponent/getScrollableBlockIncrement/
date: 2021-01-11
key: Java.J.JTextComponent
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextComponent.metodos valor="getScrollableBlockIncrement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getScrollableBlockIncrement(Rectangle visibleRect, int orientation, int direction)
~~~

## Parámetros
* **Rectangle visibleRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle visibleRect" %}
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}
* **int direction**,  {% include w3api/param_description.html metodo=_dato parametro="int direction" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextComponent](/Java/JTextComponent/)

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

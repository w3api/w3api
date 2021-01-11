---
title: AbstractBorder.getInteriorRectangle()
permalink: Java/AbstractBorder/getInteriorRectangle
date: 2021-01-11
key: JavaJava.A.AbstractBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractBorder.metodos valor="getInteriorRectangle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Rectangle getInteriorRectangle(Component c, int x, int y, int width, int height)
public static Rectangle getInteriorRectangle(Component c, Border b, int x, int y, int width, int height)
~~~

## Parámetros
* **Border b**,  {% include w3api/param_description.html metodo=_dato parametro="Border b" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[AbstractBorder](/Java/AbstractBorder/)

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

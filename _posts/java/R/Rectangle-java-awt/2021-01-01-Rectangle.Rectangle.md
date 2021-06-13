---
title: Rectangle.Rectangle()
permalink: /Java/Rectangle-java-awt/Rectangle/
date: 2021-01-11
key: Java.R.Rectangle-java-awt
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Rectangle-java-awt.constructores valor="Rectangle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Rectangle()
public Rectangle(int width, int height)
public Rectangle(int x, int y, int width, int height)
public Rectangle(Dimension d)
public Rectangle(Point p)
public Rectangle(Point p, Dimension d)
public Rectangle(Rectangle r)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **Rectangle r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle r" %}
* **Point p**,  {% include w3api/param_description.html metodo=_dato parametro="Point p" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Dimension d**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension d" %}

## Clase Padre
[Rectangle](/Java/Rectangle-java-awt/)

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

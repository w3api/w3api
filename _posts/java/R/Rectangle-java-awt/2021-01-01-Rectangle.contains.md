---
title: Rectangle.contains()
permalink: Java/Rectangle-java-awt/contains
date: 2021-01-11
key: JavaJava.R.Rectangle-java-awt
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Rectangle-java-awt.metodos valor="contains" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean contains(int x, int y)
public boolean contains(int X, int Y, int W, int H)
public boolean contains(Point p)
public boolean contains(Rectangle r)
~~~

## Parámetros
* **int Y**,  {% include w3api/param_description.html metodo=_dato parametro="int Y" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **Rectangle r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle r" %}
* **int X**,  {% include w3api/param_description.html metodo=_dato parametro="int X" %}
* **int H**,  {% include w3api/param_description.html metodo=_dato parametro="int H" %}
* **Point p**,  {% include w3api/param_description.html metodo=_dato parametro="Point p" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int W**,  {% include w3api/param_description.html metodo=_dato parametro="int W" %}

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

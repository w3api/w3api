---
title: Rectangle.add()
permalink: /Java/Rectangle-java-awt/add/
date: 2021-01-11
key: Java.R.Rectangle-java-awt
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Rectangle-java-awt.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(int newx, int newy)
public void add(Point pt)
public void add(Rectangle r)
~~~

## Parámetros
* **int newy**,  {% include w3api/param_description.html metodo=_dato parametro="int newy" %}
* **Point pt**,  {% include w3api/param_description.html metodo=_dato parametro="Point pt" %}
* **int newx**,  {% include w3api/param_description.html metodo=_dato parametro="int newx" %}
* **Rectangle r**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle r" %}

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

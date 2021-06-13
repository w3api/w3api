---
title: RoundRectangle2D.contains()
permalink: /Java/RoundRectangle2D/contains/
date: 2021-01-11
key: Java.R.RoundRectangle2D
category: Java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoundRectangle2D.metodos valor="contains" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean contains(double x, double y)
public boolean contains(double x, double y, double w, double h)
~~~

## Parámetros
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double h**,  {% include w3api/param_description.html metodo=_dato parametro="double h" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **double w**,  {% include w3api/param_description.html metodo=_dato parametro="double w" %}

## Clase Padre
[RoundRectangle2D](/Java/RoundRectangle2D/)

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

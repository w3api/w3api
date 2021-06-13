---
title: LineBorder.paintBorder()
permalink: /Java/LineBorder/paintBorder/
date: 2021-01-11
key: Java.L.LineBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineBorder.metodos valor="paintBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paintBorder(Component c, Graphics g, int x, int y, int width, int height)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[LineBorder](/Java/LineBorder/)

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

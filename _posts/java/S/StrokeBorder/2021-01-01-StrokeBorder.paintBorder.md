---
title: StrokeBorder.paintBorder()
permalink: /Java/StrokeBorder/paintBorder/
date: 2021-01-11
key: Java.S.StrokeBorder
category: Java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrokeBorder.metodos valor="paintBorder" %}

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

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StrokeBorder](/Java/StrokeBorder/)

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

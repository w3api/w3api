---
title: StrokeBorder.paintBorder()
permalink: Java/StrokeBorder/paintBorder
date: 2021-01-04
key: JavaJava.S.StrokeBorder
category: java
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
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **Component c**,  {% include w3api/param_description.html metodo=_data parametro="Component c" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

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
{%- for _ldc in site.data.Java.S.StrokeBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

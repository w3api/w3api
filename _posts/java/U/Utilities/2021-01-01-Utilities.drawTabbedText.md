---
title: Utilities.drawTabbedText()
permalink: Java/Utilities/drawTabbedText
date: 2021-01-11
key: JavaJava.U.Utilities
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Utilities.metodos valor="drawTabbedText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static float drawTabbedText(Segment s, float x, float y, Graphics2D g, TabExpander e, int startOffset)
static int drawTabbedText(Segment s, int x, int y, Graphics g, TabExpander e, int startOffset)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Segment s**,  {% include w3api/param_description.html metodo=_dato parametro="Segment s" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics2D g" %}
* **int startOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int startOffset" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **TabExpander e**,  {% include w3api/param_description.html metodo=_dato parametro="TabExpander e" %}

## Clase Padre
[Utilities](/Java/Utilities/)

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

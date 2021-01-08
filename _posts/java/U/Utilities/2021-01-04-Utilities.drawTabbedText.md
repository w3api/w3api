---
title: Utilities.drawTabbedText()
permalink: Java/Utilities/drawTabbedText
date: 2021-01-04
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
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics2D g" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **TabExpander e**,  {% include w3api/param_description.html metodo=_data parametro="TabExpander e" %}
* **int startOffset**,  {% include w3api/param_description.html metodo=_data parametro="int startOffset" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **Segment s**,  {% include w3api/param_description.html metodo=_data parametro="Segment s" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[Utilities](/Java/Utilities/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.Utilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

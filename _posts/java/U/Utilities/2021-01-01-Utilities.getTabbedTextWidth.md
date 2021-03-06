---
title: Utilities.getTabbedTextWidth()
permalink: /Java/Utilities/getTabbedTextWidth/
date: 2021-01-11
key: Java.U.Utilities
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Utilities.metodos valor="getTabbedTextWidth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static float getTabbedTextWidth(Segment s, FontMetrics metrics, float x, TabExpander e, int startOffset)
static int getTabbedTextWidth(Segment s, FontMetrics metrics, int x, TabExpander e, int startOffset)
~~~

## Parámetros
* **Segment s**,  {% include w3api/param_description.html metodo=_dato parametro="Segment s" %}
* **int startOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int startOffset" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **TabExpander e**,  {% include w3api/param_description.html metodo=_dato parametro="TabExpander e" %}
* **FontMetrics metrics**,  {% include w3api/param_description.html metodo=_dato parametro="FontMetrics metrics" %}

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

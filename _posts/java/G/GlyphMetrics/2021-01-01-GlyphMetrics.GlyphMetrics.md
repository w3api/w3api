---
title: GlyphMetrics.GlyphMetrics()
permalink: Java/GlyphMetrics/GlyphMetrics
date: 2021-01-11
key: JavaJava.G.GlyphMetrics
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphMetrics.constructores valor="GlyphMetrics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GlyphMetrics(boolean horizontal, float advanceX, float advanceY, Rectangle2D bounds, byte glyphType)
public GlyphMetrics(float advance, Rectangle2D bounds, byte glyphType)
~~~

## Parámetros
* **boolean horizontal**,  {% include w3api/param_description.html metodo=_dato parametro="boolean horizontal" %}
* **Rectangle2D bounds**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle2D bounds" %}
* **float advance**,  {% include w3api/param_description.html metodo=_dato parametro="float advance" %}
* **byte glyphType**,  {% include w3api/param_description.html metodo=_dato parametro="byte glyphType" %}
* **float advanceY**,  {% include w3api/param_description.html metodo=_dato parametro="float advanceY" %}
* **float advanceX**,  {% include w3api/param_description.html metodo=_dato parametro="float advanceX" %}

## Clase Padre
[GlyphMetrics](/Java/GlyphMetrics/)

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

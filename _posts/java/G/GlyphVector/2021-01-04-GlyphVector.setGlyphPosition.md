---
title: GlyphVector.setGlyphPosition()
permalink: Java/GlyphVector/setGlyphPosition
date: 2021-01-04
key: JavaJava.G.GlyphVector
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphVector.metodos valor="setGlyphPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setGlyphPosition(int glyphIndex, Point2D newPos)
~~~

## Parámetros
* **Point2D newPos**,  {% include w3api/param_description.html metodo=_data parametro="Point2D newPos" %}
* **int glyphIndex**,  {% include w3api/param_description.html metodo=_data parametro="int glyphIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[GlyphVector](/Java/GlyphVector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GlyphVector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

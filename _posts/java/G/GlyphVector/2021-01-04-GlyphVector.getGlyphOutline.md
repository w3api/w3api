---
title: GlyphVector.getGlyphOutline()
permalink: Java/GlyphVector/getGlyphOutline
date: 2021-01-04
key: JavaJava.G.GlyphVector
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphVector.metodos valor="getGlyphOutline" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Shape getGlyphOutline(int glyphIndex)
public Shape getGlyphOutline(int glyphIndex, float x, float y)
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
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

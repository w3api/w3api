---
title: GlyphVector.getGlyphTransform()
permalink: Java/GlyphVector/getGlyphTransform
date: 2021-01-11
key: JavaJava.G.GlyphVector
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphVector.metodos valor="getGlyphTransform" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AffineTransform getGlyphTransform(int glyphIndex)
~~~

## Parámetros
* **int glyphIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int glyphIndex" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

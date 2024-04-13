---
title: GlyphVector.getGlyphPositions()
permalink: /Java/GlyphVector/getGlyphPositions/
date: 2021-01-11
key: Java.G.GlyphVector
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphVector.metodos valor="getGlyphPositions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract float[] getGlyphPositions(int beginGlyphIndex, int numEntries, float[] positionReturn)
~~~

## Parámetros
* **float[] positionReturn**,  {% include w3api/param_description.html metodo=_dato parametro="float[] positionReturn" %}
* **int numEntries**,  {% include w3api/param_description.html metodo=_dato parametro="int numEntries" %}
* **int beginGlyphIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginGlyphIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

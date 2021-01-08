---
title: GlyphVector.getGlyphCodes()
permalink: Java/GlyphVector/getGlyphCodes
date: 2021-01-04
key: JavaJava.G.GlyphVector
category: java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GlyphVector.metodos valor="getGlyphCodes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int[] getGlyphCodes(int beginGlyphIndex, int numEntries, int[] codeReturn)
~~~

## Parámetros
* **int numEntries**,  {% include w3api/param_description.html metodo=_data parametro="int numEntries" %}
* **int beginGlyphIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginGlyphIndex" %}
* **int[] codeReturn**,  {% include w3api/param_description.html metodo=_data parametro="int[] codeReturn" %}

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
{%- for _ldc in site.data.Java.G.GlyphVector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

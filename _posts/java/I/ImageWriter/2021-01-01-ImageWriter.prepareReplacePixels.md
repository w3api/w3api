---
title: ImageWriter.prepareReplacePixels()
permalink: /Java/ImageWriter/prepareReplacePixels/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="prepareReplacePixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void prepareReplacePixels(int imageIndex, Rectangle region) throws IOException
~~~

## Parámetros
* **Rectangle region**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle region" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

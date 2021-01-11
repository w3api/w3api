---
title: ImageReader.getThumbnailHeight()
permalink: Java/ImageReader/getThumbnailHeight
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="getThumbnailHeight" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getThumbnailHeight(int imageIndex, int thumbnailIndex) throws IOException
~~~

## Parámetros
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}
* **int thumbnailIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int thumbnailIndex" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ImageReader](/Java/ImageReader/)

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

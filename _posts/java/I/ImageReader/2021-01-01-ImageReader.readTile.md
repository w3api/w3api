---
title: ImageReader.readTile()
permalink: Java/ImageReader/readTile
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="readTile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage readTile(int imageIndex, int tileX, int tileY) throws IOException
~~~

## Parámetros
* **int tileY**,  {% include w3api/param_description.html metodo=_dato parametro="int tileY" %}
* **int tileX**,  {% include w3api/param_description.html metodo=_dato parametro="int tileX" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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

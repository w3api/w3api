---
title: ImageReader.read()
permalink: Java/ImageReader/read
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferedImage read(int imageIndex) throws IOException
public abstract BufferedImage read(int imageIndex, ImageReadParam param) throws IOException
~~~

## Parámetros
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageReadParam param" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageReader](/Java/ImageReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

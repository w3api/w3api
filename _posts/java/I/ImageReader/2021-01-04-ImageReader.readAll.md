---
title: ImageReader.readAll()
permalink: Java/ImageReader/readAll
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="readAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IIOImage readAll(int imageIndex, ImageReadParam param) throws IOException
public Iterator<IIOImage> readAll(Iterator<? extends ImageReadParam> params) throws IOException
~~~

## Parámetros
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **ImageReadParam param**,  {% include w3api/param_description.html metodo=_data parametro="ImageReadParam param" %}
* **Iterator&lt;? extends ImageReadParam&gt; params**,  {% include w3api/param_description.html metodo=_data parametro="Iterator<? extends ImageReadParam> params" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

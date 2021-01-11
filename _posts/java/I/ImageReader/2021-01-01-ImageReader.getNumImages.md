---
title: ImageReader.getNumImages()
permalink: Java/ImageReader/getNumImages
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="getNumImages" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int getNumImages(boolean allowSearch) throws IOException
~~~

## Parámetros
* **boolean allowSearch**,  {% include w3api/param_description.html metodo=_dato parametro="boolean allowSearch" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

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

---
title: ImageWriter.canReplacePixels()
permalink: Java/ImageWriter/canReplacePixels
date: 2021-01-11
key: JavaJava.I.ImageWriter
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="canReplacePixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean canReplacePixels(int imageIndex) throws IOException
~~~

## Parámetros
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

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

---
title: ImageWriter.writeInsert()
permalink: Java/ImageWriter/writeInsert
date: 2021-01-11
key: JavaJava.I.ImageWriter
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="writeInsert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeInsert(int imageIndex, IIOImage image, ImageWriteParam param) throws IOException
~~~

## Parámetros
* **IIOImage image**,  {% include w3api/param_description.html metodo=_dato parametro="IIOImage image" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

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

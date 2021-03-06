---
title: ImageWriter.writeToSequence()
permalink: /Java/ImageWriter/writeToSequence/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="writeToSequence" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeToSequence(IIOImage image, ImageWriteParam param) throws IOException
~~~

## Parámetros
* **IIOImage image**,  {% include w3api/param_description.html metodo=_dato parametro="IIOImage image" %}
* **ImageWriteParam param**,  {% include w3api/param_description.html metodo=_dato parametro="ImageWriteParam param" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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

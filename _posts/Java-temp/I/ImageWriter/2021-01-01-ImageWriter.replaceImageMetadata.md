---
title: ImageWriter.replaceImageMetadata()
permalink: /Java/ImageWriter/replaceImageMetadata/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="replaceImageMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replaceImageMetadata(int imageIndex, IIOMetadata imageMetadata) throws IOException
~~~

## Parámetros
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata imageMetadata" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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

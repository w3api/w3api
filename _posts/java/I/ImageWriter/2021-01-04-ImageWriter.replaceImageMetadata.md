---
title: ImageWriter.replaceImageMetadata()
permalink: Java/ImageWriter/replaceImageMetadata
date: 2021-01-04
key: JavaJava.I.ImageWriter
category: java
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
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **IIOMetadata imageMetadata**,  {% include w3api/param_description.html metodo=_data parametro="IIOMetadata imageMetadata" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

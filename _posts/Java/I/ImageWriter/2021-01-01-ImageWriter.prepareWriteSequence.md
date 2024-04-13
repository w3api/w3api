---
title: ImageWriter.prepareWriteSequence()
permalink: /Java/ImageWriter/prepareWriteSequence/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="prepareWriteSequence" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void prepareWriteSequence(IIOMetadata streamMetadata) throws IOException
~~~

## Parámetros
* **IIOMetadata streamMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="IIOMetadata streamMetadata" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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

---
title: ImageReader.getImageMetadata()
permalink: Java/ImageReader/getImageMetadata
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="getImageMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract IIOMetadata getImageMetadata(int imageIndex) throws IOException
public IIOMetadata getImageMetadata(int imageIndex, String formatName, Set<String> nodeNames) throws IOException
~~~

## Parámetros
* **Set&lt;String&gt; nodeNames**,  {% include w3api/param_description.html metodo=_dato parametro="Set<String> nodeNames" %}
* **String formatName**,  {% include w3api/param_description.html metodo=_dato parametro="String formatName" %}
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

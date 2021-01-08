---
title: ImageReader.getStreamMetadata()
permalink: Java/ImageReader/getStreamMetadata
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="getStreamMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract IIOMetadata getStreamMetadata() throws IOException
public IIOMetadata getStreamMetadata(String formatName, Set<String> nodeNames) throws IOException
~~~

## Parámetros
* **Set&lt;String&gt; nodeNames**,  {% include w3api/param_description.html metodo=_data parametro="Set<String> nodeNames" %}
* **String formatName**,  {% include w3api/param_description.html metodo=_data parametro="String formatName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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

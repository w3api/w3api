---
title: FileChannel.map()
permalink: Java/FileChannel/map
date: 2021-01-04
key: JavaJava.F.FileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="map" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract MappedByteBuffer map(FileChannel.MapMode mode, long position, long size) throws IOException
~~~

## Parámetros
* **long position**,  {% include w3api/param_description.html metodo=_data parametro="long position" %}
* **FileChannel.MapMode mode**,  {% include w3api/param_description.html metodo=_data parametro="FileChannel.MapMode mode" %}
* **long size**,  {% include w3api/param_description.html metodo=_data parametro="long size" %}

## Excepciones
[IOException](/Java/IOException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [NonReadableChannelException](/Java/NonReadableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FileChannel](/Java/FileChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: FileChannel.map()
permalink: Java/FileChannel/map
date: 2021-01-11
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
* **long size**,  {% include w3api/param_description.html metodo=_dato parametro="long size" %}
* **FileChannel.MapMode mode**,  {% include w3api/param_description.html metodo=_dato parametro="FileChannel.MapMode mode" %}
* **long position**,  {% include w3api/param_description.html metodo=_dato parametro="long position" %}

## Excepciones
[NonReadableChannelException](/Java/NonReadableChannelException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[FileChannel](/Java/FileChannel/)

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

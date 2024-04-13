---
title: FileChannel.truncate()
permalink: /Java/FileChannel/truncate/
date: 2021-01-11
key: Java.F.FileChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="truncate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract FileChannel truncate(long size) throws IOException
~~~

## Parámetros
* **long size**,  {% include w3api/param_description.html metodo=_dato parametro="long size" %}

## Excepciones
[NonWritableChannelException](/Java/NonWritableChannelException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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

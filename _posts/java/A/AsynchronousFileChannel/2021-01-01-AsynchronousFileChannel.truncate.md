---
title: AsynchronousFileChannel.truncate()
permalink: Java/AsynchronousFileChannel/truncate
date: 2021-01-11
key: JavaJava.A.AsynchronousFileChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousFileChannel.metodos valor="truncate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AsynchronousFileChannel truncate(long size) throws IOException
~~~

## Parámetros
* **long size**,  {% include w3api/param_description.html metodo=_dato parametro="long size" %}

## Excepciones
[NonWritableChannelException](/Java/NonWritableChannelException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[AsynchronousFileChannel](/Java/AsynchronousFileChannel/)

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

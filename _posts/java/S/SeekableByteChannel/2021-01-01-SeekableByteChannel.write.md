---
title: SeekableByteChannel.write()
permalink: Java/SeekableByteChannel/write
date: 2021-01-11
key: JavaJava.S.SeekableByteChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SeekableByteChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int write(ByteBuffer src) throws IOException
~~~

## Parámetros
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [IOException](/Java/IOException/)

## Clase Padre
[SeekableByteChannel](/Java/SeekableByteChannel/)

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

---
title: SeekableByteChannel.read()
permalink: Java/SeekableByteChannel/read
date: 2021-01-11
key: JavaJava.S.SeekableByteChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SeekableByteChannel.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int read(ByteBuffer dst) throws IOException
~~~

## Parámetros
* **ByteBuffer dst**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer dst" %}

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

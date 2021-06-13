---
title: WritableByteChannel.write()
permalink: /Java/WritableByteChannel/write/
date: 2021-01-11
key: Java.W.WritableByteChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableByteChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int write(ByteBuffer src) throws IOException
~~~

## Parámetros
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer src" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

## Clase Padre
[WritableByteChannel](/Java/WritableByteChannel/)

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

---
title: FileChannel.transferTo()
permalink: /Java/FileChannel/transferTo/
date: 2021-01-11
key: Java.F.FileChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileChannel.metodos valor="transferTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract long transferTo(long position, long count, WritableByteChannel target) throws IOException
~~~

## Parámetros
* **WritableByteChannel target**,  {% include w3api/param_description.html metodo=_dato parametro="WritableByteChannel target" %}
* **long count**,  {% include w3api/param_description.html metodo=_dato parametro="long count" %}
* **long position**,  {% include w3api/param_description.html metodo=_dato parametro="long position" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [NonReadableChannelException](/Java/NonReadableChannelException/)

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

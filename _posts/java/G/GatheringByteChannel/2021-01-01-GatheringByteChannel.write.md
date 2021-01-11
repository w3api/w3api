---
title: GatheringByteChannel.write()
permalink: Java/GatheringByteChannel/write
date: 2021-01-11
key: JavaJava.G.GatheringByteChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GatheringByteChannel.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long write(ByteBuffer[] srcs) throws IOException
long write(ByteBuffer[] srcs, int offset, int length) throws IOException
~~~

## Parámetros
* **ByteBuffer[] srcs**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer[] srcs" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[ClosedByInterruptException](/Java/ClosedByInterruptException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [NonWritableChannelException](/Java/NonWritableChannelException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/)

## Clase Padre
[GatheringByteChannel](/Java/GatheringByteChannel/)

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

---
title: GatheringByteChannel.write()
permalink: Java/GatheringByteChannel/write
date: 2021-01-04
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **ByteBuffer[] srcs**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer[] srcs" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[NonWritableChannelException](/Java/NonWritableChannelException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ClosedByInterruptException](/Java/ClosedByInterruptException/), [AsynchronousCloseException](/Java/AsynchronousCloseException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[GatheringByteChannel](/Java/GatheringByteChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GatheringByteChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

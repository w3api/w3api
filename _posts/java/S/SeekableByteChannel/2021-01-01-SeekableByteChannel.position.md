---
title: SeekableByteChannel.position()
permalink: /Java/SeekableByteChannel/position/
date: 2021-01-11
key: Java.S.SeekableByteChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SeekableByteChannel.metodos valor="position" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long position() throws IOException
SeekableByteChannel position(long newPosition) throws IOException
~~~

## Parámetros
* **long newPosition**,  {% include w3api/param_description.html metodo=_dato parametro="long newPosition" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

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

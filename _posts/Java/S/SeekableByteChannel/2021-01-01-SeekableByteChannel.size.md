---
title: SeekableByteChannel.size()
permalink: /Java/SeekableByteChannel/size/
date: 2021-01-11
key: Java.S.SeekableByteChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SeekableByteChannel.metodos valor="size" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long size() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

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

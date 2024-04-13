---
title: DatagramChannel.getRemoteAddress()
permalink: /Java/DatagramChannel/getRemoteAddress/
date: 2021-01-11
key: Java.D.DatagramChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramChannel.metodos valor="getRemoteAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SocketAddress getRemoteAddress() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[DatagramChannel](/Java/DatagramChannel/)

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

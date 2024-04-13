---
title: SctpChannel.getRemoteAddresses()
permalink: /Java/SctpChannel/getRemoteAddresses/
date: 2021-01-11
key: Java.S.SctpChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="getRemoteAddresses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Set<SocketAddress> getRemoteAddresses() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[SctpChannel](/Java/SctpChannel/)

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

---
title: SctpServerChannel.getAllLocalAddresses()
permalink: /Java/SctpServerChannel/getAllLocalAddresses/
date: 2021-01-11
key: Java.S.SctpServerChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpServerChannel.metodos valor="getAllLocalAddresses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Set<SocketAddress> getAllLocalAddresses() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[SctpServerChannel](/Java/SctpServerChannel/)

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

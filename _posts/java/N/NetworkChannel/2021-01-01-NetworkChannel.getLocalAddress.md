---
title: NetworkChannel.getLocalAddress()
permalink: Java/NetworkChannel/getLocalAddress
date: 2021-01-11
key: JavaJava.N.NetworkChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkChannel.metodos valor="getLocalAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SocketAddress getLocalAddress() throws IOException
~~~

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[NetworkChannel](/Java/NetworkChannel/)

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

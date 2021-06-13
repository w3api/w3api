---
title: SctpMultiChannel.bind()
permalink: /Java/SctpMultiChannel/bind/
date: 2021-01-11
key: Java.S.SctpMultiChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpMultiChannel.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final SctpMultiChannel bind(SocketAddress local) throws IOException
public abstract SctpMultiChannel bind(SocketAddress local, int backlog) throws IOException
~~~

## Parámetros
* **SocketAddress local**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress local" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[SctpMultiChannel](/Java/SctpMultiChannel/)

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

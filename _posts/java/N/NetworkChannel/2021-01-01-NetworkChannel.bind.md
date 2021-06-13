---
title: NetworkChannel.bind()
permalink: Java/NetworkChannel/bind
date: 2021-01-11
key: JavaJava.N.NetworkChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkChannel.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
NetworkChannel bind(SocketAddress local) throws IOException
~~~

## Parámetros
* **SocketAddress local**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress local" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [UnsupportedAddressTypeException](/Java/UnsupportedAddressTypeException/), [SecurityException](/Java/SecurityException/)

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

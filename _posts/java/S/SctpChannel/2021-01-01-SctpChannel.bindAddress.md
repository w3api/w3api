---
title: SctpChannel.bindAddress()
permalink: /Java/SctpChannel/bindAddress/
date: 2021-01-11
key: Java.S.SctpChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SctpChannel.metodos valor="bindAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SctpChannel bindAddress(InetAddress address) throws IOException
~~~

## Parámetros
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [AlreadyBoundException](/Java/AlreadyBoundException/), [NotYetBoundException](/Java/NotYetBoundException/), [ConnectionPendingException](/Java/ConnectionPendingException/)

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

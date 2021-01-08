---
title: DatagramSocket.connect()
permalink: Java/DatagramSocket/connect
date: 2021-01-04
key: JavaJava.D.DatagramSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void connect(InetAddress address, int port)
public void connect(SocketAddress addr) throws SocketException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **SocketAddress addr**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress addr" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress address" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [SocketException](/Java/SocketException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DatagramSocket](/Java/DatagramSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

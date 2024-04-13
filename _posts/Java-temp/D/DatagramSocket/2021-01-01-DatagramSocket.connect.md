---
title: DatagramSocket.connect()
permalink: /Java/DatagramSocket/connect/
date: 2021-01-11
key: Java.D.DatagramSocket
category: Java
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
* **SocketAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress addr" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [SocketException](/Java/SocketException/)

## Clase Padre
[DatagramSocket](/Java/DatagramSocket/)

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

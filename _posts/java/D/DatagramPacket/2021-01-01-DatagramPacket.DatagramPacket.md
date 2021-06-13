---
title: DatagramPacket.DatagramPacket()
permalink: /Java/DatagramPacket/DatagramPacket/
date: 2021-01-11
key: Java.D.DatagramPacket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramPacket.constructores valor="DatagramPacket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DatagramPacket(byte[] buf, int length)
public DatagramPacket(byte[] buf, int offset, int length)
public DatagramPacket(byte[] buf, int offset, int length, InetAddress address, int port)
public DatagramPacket(byte[] buf, int offset, int length, SocketAddress address)
public DatagramPacket(byte[] buf, int length, InetAddress address, int port)
public DatagramPacket(byte[] buf, int length, SocketAddress address)
~~~

## Parámetros
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **SocketAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress address" %}
* **byte[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buf" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DatagramPacket](/Java/DatagramPacket/)

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

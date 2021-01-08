---
title: DatagramPacket.DatagramPacket()
permalink: Java/DatagramPacket/DatagramPacket
date: 2021-01-04
key: JavaJava.D.DatagramPacket
category: java
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
* **byte[] buf**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buf" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress address" %}
* **SocketAddress address**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress address" %}

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
{%- for _ldc in site.data.Java.D.DatagramPacket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

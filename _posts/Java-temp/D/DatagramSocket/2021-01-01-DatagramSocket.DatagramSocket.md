---
title: DatagramSocket.DatagramSocket()
permalink: /Java/DatagramSocket/DatagramSocket/
date: 2021-01-11
key: Java.D.DatagramSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.constructores valor="DatagramSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DatagramSocket() throws SocketException
public DatagramSocket(int port) throws SocketException
public DatagramSocket(int port, InetAddress laddr) throws SocketException
protected DatagramSocket(DatagramSocketImpl impl)
public DatagramSocket(SocketAddress bindaddr) throws SocketException
~~~

## Parámetros
* **InetAddress laddr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress laddr" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **SocketAddress bindaddr**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress bindaddr" %}
* **DatagramSocketImpl impl**,  {% include w3api/param_description.html metodo=_dato parametro="DatagramSocketImpl impl" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [SocketException](/Java/SocketException/)

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

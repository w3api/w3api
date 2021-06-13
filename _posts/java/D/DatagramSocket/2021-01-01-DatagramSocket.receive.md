---
title: DatagramSocket.receive()
permalink: /Java/DatagramSocket/receive/
date: 2021-01-11
key: Java.D.DatagramSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="receive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void receive(DatagramPacket p) throws IOException
~~~

## Parámetros
* **DatagramPacket p**,  {% include w3api/param_description.html metodo=_dato parametro="DatagramPacket p" %}

## Excepciones
[PortUnreachableException](/Java/PortUnreachableException/), [SocketTimeoutException](/Java/SocketTimeoutException/), [IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [IOException](/Java/IOException/)

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

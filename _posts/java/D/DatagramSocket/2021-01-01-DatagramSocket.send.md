---
title: DatagramSocket.send()
permalink: /Java/DatagramSocket/send/
date: 2021-01-11
key: Java.D.DatagramSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="send" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void send(DatagramPacket p) throws IOException
~~~

## Parámetros
* **DatagramPacket p**,  {% include w3api/param_description.html metodo=_dato parametro="DatagramPacket p" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [SecurityException](/Java/SecurityException/), [PortUnreachableException](/Java/PortUnreachableException/)

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

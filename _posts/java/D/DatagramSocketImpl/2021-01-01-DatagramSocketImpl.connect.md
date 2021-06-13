---
title: DatagramSocketImpl.connect()
permalink: /Java/DatagramSocketImpl/connect/
date: 2021-01-11
key: Java.D.DatagramSocketImpl
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocketImpl.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void connect(InetAddress address, int port) throws SocketException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[DatagramSocketImpl](/Java/DatagramSocketImpl/)

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

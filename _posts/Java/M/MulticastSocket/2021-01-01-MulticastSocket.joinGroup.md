---
title: MulticastSocket.joinGroup()
permalink: /Java/MulticastSocket/joinGroup/
date: 2021-01-11
key: Java.M.MulticastSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.metodos valor="joinGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void joinGroup(InetAddress mcastaddr) throws IOException
public void joinGroup(SocketAddress mcastaddr, NetworkInterface netIf) throws IOException
~~~

## Parámetros
* **SocketAddress mcastaddr**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress mcastaddr" %}
* **NetworkInterface netIf**,  {% include w3api/param_description.html metodo=_dato parametro="NetworkInterface netIf" %}
* **InetAddress mcastaddr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress mcastaddr" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[MulticastSocket](/Java/MulticastSocket/)

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

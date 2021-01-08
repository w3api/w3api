---
title: MulticastSocket.MulticastSocket()
permalink: Java/MulticastSocket/MulticastSocket
date: 2021-01-04
key: JavaJava.M.MulticastSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.constructores valor="MulticastSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MulticastSocket() throws IOException
public MulticastSocket(int port) throws IOException
public MulticastSocket(SocketAddress bindaddr) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **SocketAddress bindaddr**,  {% include w3api/param_description.html metodo=_data parametro="SocketAddress bindaddr" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[MulticastSocket](/Java/MulticastSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MulticastSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

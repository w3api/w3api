---
title: MulticastSocket.send()
permalink: /Java/MulticastSocket/send/
date: 2021-01-11
key: Java.M.MulticastSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.metodos valor="send" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public void send(DatagramPacket p, byte ttl) throws IOException
~~~

## Parámetros
* **byte ttl**,  {% include w3api/param_description.html metodo=_dato parametro="byte ttl" %}
* **DatagramPacket p**,  {% include w3api/param_description.html metodo=_dato parametro="DatagramPacket p" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

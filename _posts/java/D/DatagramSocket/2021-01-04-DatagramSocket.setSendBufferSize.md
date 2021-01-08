---
title: DatagramSocket.setSendBufferSize()
permalink: Java/DatagramSocket/setSendBufferSize
date: 2021-01-04
key: JavaJava.D.DatagramSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="setSendBufferSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSendBufferSize(int size) throws SocketException
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}

## Excepciones
[SocketException](/Java/SocketException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DatagramSocket](/Java/DatagramSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

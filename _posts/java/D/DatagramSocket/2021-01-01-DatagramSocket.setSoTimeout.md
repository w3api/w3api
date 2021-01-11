---
title: DatagramSocket.setSoTimeout()
permalink: Java/DatagramSocket/setSoTimeout
date: 2021-01-11
key: JavaJava.D.DatagramSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="setSoTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSoTimeout(int timeout) throws SocketException
~~~

## Parámetros
* **int timeout**,  {% include w3api/param_description.html metodo=_dato parametro="int timeout" %}

## Excepciones
[SocketException](/Java/SocketException/)

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

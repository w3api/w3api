---
title: NetworkInterface.getByInetAddress()
permalink: Java/NetworkInterface/getByInetAddress
date: 2021-01-04
key: JavaJava.N.NetworkInterface
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkInterface.metodos valor="getByInetAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static NetworkInterface getByInetAddress(InetAddress addr) throws SocketException
~~~

## Parámetros
* **InetAddress addr**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress addr" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [SocketException](/Java/SocketException/)

## Clase Padre
[NetworkInterface](/Java/NetworkInterface/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NetworkInterface.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

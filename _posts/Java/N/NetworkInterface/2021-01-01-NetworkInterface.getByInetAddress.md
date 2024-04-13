---
title: NetworkInterface.getByInetAddress()
permalink: /Java/NetworkInterface/getByInetAddress/
date: 2021-01-11
key: Java.N.NetworkInterface
category: Java
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
* **InetAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress addr" %}

## Excepciones
[SocketException](/Java/SocketException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NetworkInterface](/Java/NetworkInterface/)

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

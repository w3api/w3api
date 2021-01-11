---
title: NetworkInterface.getNetworkInterfaces()
permalink: Java/NetworkInterface/getNetworkInterfaces
date: 2021-01-11
key: JavaJava.N.NetworkInterface
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkInterface.metodos valor="getNetworkInterfaces" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Enumeration<NetworkInterface> getNetworkInterfaces() throws SocketException
~~~

## Excepciones
[SocketException](/Java/SocketException/)

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
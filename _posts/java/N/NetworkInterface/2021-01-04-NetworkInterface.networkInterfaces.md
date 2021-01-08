---
title: NetworkInterface.networkInterfaces()
permalink: Java/NetworkInterface/networkInterfaces
date: 2021-01-04
key: JavaJava.N.NetworkInterface
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkInterface.metodos valor="networkInterfaces" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Stream<NetworkInterface> networkInterfaces() throws SocketException
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
{%- for _ldc in site.data.Java.N.NetworkInterface.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

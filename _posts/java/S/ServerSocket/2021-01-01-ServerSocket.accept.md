---
title: ServerSocket.accept()
permalink: Java/ServerSocket/accept
date: 2021-01-11
key: JavaJava.S.ServerSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocket.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Socket accept() throws IOException
~~~

## Excepciones
[IllegalBlockingModeException](/Java/IllegalBlockingModeException/), [SecurityException](/Java/SecurityException/), [SocketTimeoutException](/Java/SocketTimeoutException/), [IOException](/Java/IOException/)

## Clase Padre
[ServerSocket](/Java/ServerSocket/)

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

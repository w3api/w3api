---
title: ServerSocket.setSocketFactory()
permalink: /Java/ServerSocket/setSocketFactory/
date: 2021-01-11
key: Java.S.ServerSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocket.metodos valor="setSocketFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setSocketFactory(SocketImplFactory fac) throws IOException
~~~

## Parámetros
* **SocketImplFactory fac**,  {% include w3api/param_description.html metodo=_dato parametro="SocketImplFactory fac" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [SocketException](/Java/SocketException/), [IOException](/Java/IOException/)

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

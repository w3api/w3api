---
title: ServerSocket.setReuseAddress()
permalink: Java/ServerSocket/setReuseAddress
date: 2021-01-11
key: JavaJava.S.ServerSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocket.metodos valor="setReuseAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setReuseAddress(boolean on) throws SocketException
~~~

## Parámetros
* **boolean on**,  {% include w3api/param_description.html metodo=_dato parametro="boolean on" %}

## Excepciones
[SocketException](/Java/SocketException/)

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
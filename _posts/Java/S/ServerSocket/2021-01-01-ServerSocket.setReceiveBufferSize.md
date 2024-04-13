---
title: ServerSocket.setReceiveBufferSize()
permalink: /Java/ServerSocket/setReceiveBufferSize/
date: 2021-01-11
key: Java.S.ServerSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocket.metodos valor="setReceiveBufferSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setReceiveBufferSize(int size) throws SocketException
~~~

## Parámetros
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Excepciones
[SocketException](/Java/SocketException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

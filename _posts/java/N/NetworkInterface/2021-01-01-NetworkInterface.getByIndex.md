---
title: NetworkInterface.getByIndex()
permalink: Java/NetworkInterface/getByIndex
date: 2021-01-11
key: JavaJava.N.NetworkInterface
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkInterface.metodos valor="getByIndex" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static NetworkInterface getByIndex(int index) throws SocketException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[SocketException](/Java/SocketException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

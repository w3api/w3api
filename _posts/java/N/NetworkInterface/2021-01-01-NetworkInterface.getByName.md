---
title: NetworkInterface.getByName()
permalink: Java/NetworkInterface/getByName
date: 2021-01-11
key: JavaJava.N.NetworkInterface
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NetworkInterface.metodos valor="getByName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static NetworkInterface getByName(String name) throws SocketException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

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

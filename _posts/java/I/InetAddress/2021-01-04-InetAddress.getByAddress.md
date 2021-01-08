---
title: InetAddress.getByAddress()
permalink: Java/InetAddress/getByAddress
date: 2021-01-04
key: JavaJava.I.InetAddress
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InetAddress.metodos valor="getByAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static InetAddress getByAddress(byte[] addr) throws UnknownHostException
public static InetAddress getByAddress(String host, byte[] addr) throws UnknownHostException
~~~

## Parámetros
* **byte[] addr**,  {% include w3api/param_description.html metodo=_data parametro="byte[] addr" %}
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}

## Excepciones
[UnknownHostException](/Java/UnknownHostException/)

## Clase Padre
[InetAddress](/Java/InetAddress/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InetAddress.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

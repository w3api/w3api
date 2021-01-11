---
title: InetAddress.isReachable()
permalink: Java/InetAddress/isReachable
date: 2021-01-11
key: JavaJava.I.InetAddress
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InetAddress.metodos valor="isReachable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isReachable(int timeout) throws IOException
public boolean isReachable(NetworkInterface netif, int ttl, int timeout) throws IOException
~~~

## Parámetros
* **int timeout**,  {% include w3api/param_description.html metodo=_dato parametro="int timeout" %}
* **int ttl**,  {% include w3api/param_description.html metodo=_dato parametro="int ttl" %}
* **NetworkInterface netif**,  {% include w3api/param_description.html metodo=_dato parametro="NetworkInterface netif" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[InetAddress](/Java/InetAddress/)

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

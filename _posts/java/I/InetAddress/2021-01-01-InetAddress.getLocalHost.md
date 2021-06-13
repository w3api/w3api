---
title: InetAddress.getLocalHost()
permalink: /Java/InetAddress/getLocalHost/
date: 2021-01-11
key: Java.I.InetAddress
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InetAddress.metodos valor="getLocalHost" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static InetAddress getLocalHost() throws UnknownHostException
~~~

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: InetAddress.getAllByName()
permalink: Java/InetAddress/getAllByName
date: 2021-01-04
key: JavaJava.I.InetAddress
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InetAddress.metodos valor="getAllByName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static InetAddress[] getAllByName(String host) throws UnknownHostException
~~~

## Parámetros
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [UnknownHostException](/Java/UnknownHostException/)

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

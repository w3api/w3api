---
title: ProxySelector.of()
permalink: Java/ProxySelector/of
date: 2021-01-11
key: JavaJava.P.ProxySelector
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProxySelector.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ProxySelector of(InetSocketAddress proxyAddress)
~~~

## Parámetros
* **InetSocketAddress proxyAddress**,  {% include w3api/param_description.html metodo=_dato parametro="InetSocketAddress proxyAddress" %}

## Clase Padre
[ProxySelector](/Java/ProxySelector/)

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

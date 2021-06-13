---
title: SimpleMeter.request()
permalink: /Java/SimpleMeter/request/
date: 2021-01-11
key: Java.S.SimpleMeter
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleMeter.metodos valor="request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long request(long amount, ResourceId id)
~~~

## Parámetros
* **long amount**,  {% include w3api/param_description.html metodo=_dato parametro="long amount" %}
* **ResourceId id**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceId id" %}

## Clase Padre
[SimpleMeter](/Java/SimpleMeter/)

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

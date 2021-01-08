---
title: LockSupport.parkNanos()
permalink: Java/LockSupport/parkNanos
date: 2021-01-04
key: JavaJava.L.LockSupport
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LockSupport.metodos valor="parkNanos" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void parkNanos(long nanos)
public static void parkNanos(Object blocker, long nanos)
~~~

## Parámetros
* **Object blocker**,  {% include w3api/param_description.html metodo=_data parametro="Object blocker" %}
* **long nanos**,  {% include w3api/param_description.html metodo=_data parametro="long nanos" %}

## Clase Padre
[LockSupport](/Java/LockSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LockSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: ThreadPoolExecutor.getKeepAliveTime()
permalink: /Java/ThreadPoolExecutor/getKeepAliveTime/
date: 2021-01-11
key: Java.T.ThreadPoolExecutor
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="getKeepAliveTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long getKeepAliveTime(TimeUnit unit)
~~~

## Parámetros
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Clase Padre
[ThreadPoolExecutor](/Java/ThreadPoolExecutor/)

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

---
title: ThreadPoolExecutor.setKeepAliveTime()
permalink: Java/ThreadPoolExecutor/setKeepAliveTime
date: 2021-01-11
key: JavaJava.T.ThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="setKeepAliveTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setKeepAliveTime(long time, TimeUnit unit)
~~~

## Parámetros
* **long time**,  {% include w3api/param_description.html metodo=_dato parametro="long time" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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

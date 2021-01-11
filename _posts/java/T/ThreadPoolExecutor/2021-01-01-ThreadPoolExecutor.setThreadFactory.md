---
title: ThreadPoolExecutor.setThreadFactory()
permalink: Java/ThreadPoolExecutor/setThreadFactory
date: 2021-01-11
key: JavaJava.T.ThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="setThreadFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setThreadFactory(ThreadFactory threadFactory)
~~~

## Parámetros
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadFactory threadFactory" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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

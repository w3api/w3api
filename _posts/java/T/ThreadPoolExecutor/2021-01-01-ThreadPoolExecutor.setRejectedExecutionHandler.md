---
title: ThreadPoolExecutor.setRejectedExecutionHandler()
permalink: /Java/ThreadPoolExecutor/setRejectedExecutionHandler/
date: 2021-01-11
key: Java.T.ThreadPoolExecutor
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="setRejectedExecutionHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setRejectedExecutionHandler(RejectedExecutionHandler handler)
~~~

## Parámetros
* **RejectedExecutionHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="RejectedExecutionHandler handler" %}

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

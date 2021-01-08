---
title: ThreadPoolExecutor.allowCoreThreadTimeOut()
permalink: Java/ThreadPoolExecutor/allowCoreThreadTimeOut
date: 2021-01-04
key: JavaJava.T.ThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.metodos valor="allowCoreThreadTimeOut" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void allowCoreThreadTimeOut(boolean value)
~~~

## Parámetros
* **boolean value**,  {% include w3api/param_description.html metodo=_data parametro="boolean value" %}

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
{%- for _ldc in site.data.Java.T.ThreadPoolExecutor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

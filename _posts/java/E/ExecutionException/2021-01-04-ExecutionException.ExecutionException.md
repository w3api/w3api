---
title: ExecutionException.ExecutionException()
permalink: Java/ExecutionException/ExecutionException
date: 2021-01-04
key: JavaJava.E.ExecutionException
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutionException.constructores valor="ExecutionException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ExecutionException()
protected ExecutionException(String message)
public ExecutionException(String message, Throwable cause)
public ExecutionException(Throwable cause)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[ExecutionException](/Java/ExecutionException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutionException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

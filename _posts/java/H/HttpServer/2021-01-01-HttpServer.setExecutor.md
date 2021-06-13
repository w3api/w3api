---
title: HttpServer.setExecutor()
permalink: /Java/HttpServer/setExecutor/
date: 2021-01-11
key: Java.H.HttpServer
category: Java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpServer.metodos valor="setExecutor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setExecutor(Executor executor)
~~~

## Parámetros
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[HttpServer](/Java/HttpServer/)

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

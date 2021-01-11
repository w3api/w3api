---
title: JavaFileManager.getServiceLoader()
permalink: Java/JavaFileManager/getServiceLoader
date: 2021-01-11
key: JavaJava.J.JavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="getServiceLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default <S> ServiceLoader<S> getServiceLoader(JavaFileManager.Location location, Class<S> service)
~~~

## Parámetros
* **Class&lt;S&gt; service**,  {% include w3api/param_description.html metodo=_dato parametro="Class<S> service" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

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

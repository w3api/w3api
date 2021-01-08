---
title: LoaderHandler.loadClass()
permalink: Java/LoaderHandler/loadClass
date: 2021-01-04
key: JavaJava.L.LoaderHandler
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoaderHandler.metodos valor="loadClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated Class<?> loadClass(String name) throws MalformedURLException, ClassNotFoundException
@Deprecated Class<?> loadClass(URL codebase, String name) throws MalformedURLException, ClassNotFoundException
~~~

## Parámetros
* **URL codebase**,  {% include w3api/param_description.html metodo=_data parametro="URL codebase" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [MalformedURLException](/Java/MalformedURLException/)

## Clase Padre
[LoaderHandler](/Java/LoaderHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LoaderHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: RMIClassLoader.loadClass()
permalink: Java/RMIClassLoader/loadClass
date: 2021-01-04
key: JavaJava.R.RMIClassLoader
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIClassLoader.metodos valor="loadClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public static Class<?> loadClass(String name) throws MalformedURLException, ClassNotFoundException
public static Class<?> loadClass(String codebase, String name) throws MalformedURLException, ClassNotFoundException
public static Class<?> loadClass(String codebase, String name, ClassLoader defaultLoader) throws MalformedURLException, ClassNotFoundException
public static Class<?> loadClass(URL codebase, String name) throws MalformedURLException, ClassNotFoundException
~~~

## Parámetros
* **URL codebase**,  {% include w3api/param_description.html metodo=_data parametro="URL codebase" %}
* **String codebase**,  {% include w3api/param_description.html metodo=_data parametro="String codebase" %}
* **ClassLoader defaultLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader defaultLoader" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [MalformedURLException](/Java/MalformedURLException/)

## Clase Padre
[RMIClassLoader](/Java/RMIClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: RMIClassLoaderSpi.loadClass()
permalink: Java/RMIClassLoaderSpi/loadClass
date: 2021-01-11
key: Java.R.RMIClassLoaderSpi
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIClassLoaderSpi.metodos valor="loadClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Class<?> loadClass(String codebase, String name, ClassLoader defaultLoader) throws MalformedURLException, ClassNotFoundException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String codebase**,  {% include w3api/param_description.html metodo=_dato parametro="String codebase" %}
* **ClassLoader defaultLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader defaultLoader" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [MalformedURLException](/Java/MalformedURLException/)

## Clase Padre
[RMIClassLoaderSpi](/Java/RMIClassLoaderSpi/)

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

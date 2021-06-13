---
title: RMIClassLoaderSpi.loadProxyClass()
permalink: /Java/RMIClassLoaderSpi/loadProxyClass/
date: 2021-01-11
key: Java.R.RMIClassLoaderSpi
category: Java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIClassLoaderSpi.metodos valor="loadProxyClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Class<?> loadProxyClass(String codebase, String[] interfaces, ClassLoader defaultLoader) throws MalformedURLException, ClassNotFoundException
~~~

## Parámetros
* **ClassLoader defaultLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader defaultLoader" %}
* **String[] interfaces**,  {% include w3api/param_description.html metodo=_dato parametro="String[] interfaces" %}
* **String codebase**,  {% include w3api/param_description.html metodo=_dato parametro="String codebase" %}

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

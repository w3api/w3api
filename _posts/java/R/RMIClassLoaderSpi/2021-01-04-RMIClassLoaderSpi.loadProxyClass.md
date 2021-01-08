---
title: RMIClassLoaderSpi.loadProxyClass()
permalink: Java/RMIClassLoaderSpi/loadProxyClass
date: 2021-01-04
key: JavaJava.R.RMIClassLoaderSpi
category: java
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
* **String codebase**,  {% include w3api/param_description.html metodo=_data parametro="String codebase" %}
* **ClassLoader defaultLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader defaultLoader" %}
* **String[] interfaces**,  {% include w3api/param_description.html metodo=_data parametro="String[] interfaces" %}

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
{%- for _ldc in site.data.Java.R.RMIClassLoaderSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

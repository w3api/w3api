---
title: RMIClassLoader.getClassLoader()
permalink: Java/RMIClassLoader/getClassLoader
date: 2021-01-11
key: JavaJava.R.RMIClassLoader
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIClassLoader.metodos valor="getClassLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ClassLoader getClassLoader(String codebase) throws MalformedURLException, SecurityException
~~~

## Parámetros
* **String codebase**,  {% include w3api/param_description.html metodo=_dato parametro="String codebase" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [MalformedURLException](/Java/MalformedURLException/)

## Clase Padre
[RMIClassLoader](/Java/RMIClassLoader/)

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

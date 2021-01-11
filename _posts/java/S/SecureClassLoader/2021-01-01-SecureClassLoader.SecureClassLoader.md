---
title: SecureClassLoader.SecureClassLoader()
permalink: Java/SecureClassLoader/SecureClassLoader
date: 2021-01-11
key: JavaJava.S.SecureClassLoader
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureClassLoader.constructores valor="SecureClassLoader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SecureClassLoader()
protected SecureClassLoader(ClassLoader parent)
protected SecureClassLoader(String name, ClassLoader parent)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ClassLoader parent**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader parent" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SecureClassLoader](/Java/SecureClassLoader/)

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

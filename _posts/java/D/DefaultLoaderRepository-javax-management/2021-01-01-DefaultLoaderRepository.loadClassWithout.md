---
title: DefaultLoaderRepository.loadClassWithout()
permalink: /Java/DefaultLoaderRepository-javax-management/loadClassWithout/
date: 2021-01-11
key: Java.D.DefaultLoaderRepository-javax-management
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultLoaderRepository-javax-management.metodos valor="loadClassWithout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Class<?> loadClassWithout(ClassLoader loader, String className) throws ClassNotFoundException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[DefaultLoaderRepository](/Java/DefaultLoaderRepository-javax-management/)

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

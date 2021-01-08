---
title: DefaultLoaderRepository.loadClassWithout()
permalink: Java/DefaultLoaderRepository-javax-management/loadClassWithout
date: 2021-01-04
key: JavaJava.D.DefaultLoaderRepository-javax-management
category: java
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader loader" %}

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
{%- for _ldc in site.data.Java.D.DefaultLoaderRepository-javax-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: ClassLoaderRepository.loadClassWithout()
permalink: /Java/ClassLoaderRepository/loadClassWithout/
date: 2021-01-11
key: Java.C.ClassLoaderRepository
category: Java
tags: ['java se', 'javax.management.loading', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoaderRepository.metodos valor="loadClassWithout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Class<?> loadClassWithout(ClassLoader exclude, String className) throws ClassNotFoundException
~~~

## Parámetros
* **ClassLoader exclude**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader exclude" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[ClassLoaderRepository](/Java/ClassLoaderRepository/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

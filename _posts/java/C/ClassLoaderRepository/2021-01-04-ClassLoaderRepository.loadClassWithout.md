---
title: ClassLoaderRepository.loadClassWithout()
permalink: Java/ClassLoaderRepository/loadClassWithout
date: 2021-01-04
key: JavaJava.C.ClassLoaderRepository
category: java
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **ClassLoader exclude**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader exclude" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[ClassLoaderRepository](/Java/ClassLoaderRepository/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoaderRepository.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

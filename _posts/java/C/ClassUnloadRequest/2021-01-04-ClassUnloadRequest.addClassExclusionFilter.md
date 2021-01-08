---
title: ClassUnloadRequest.addClassExclusionFilter()
permalink: Java/ClassUnloadRequest/addClassExclusionFilter
date: 2021-01-04
key: JavaJava.C.ClassUnloadRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassUnloadRequest.metodos valor="addClassExclusionFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addClassExclusionFilter(String classPattern)
~~~

## Parámetros
* **String classPattern**,  {% include w3api/param_description.html metodo=_data parametro="String classPattern" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/)

## Clase Padre
[ClassUnloadRequest](/Java/ClassUnloadRequest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassUnloadRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

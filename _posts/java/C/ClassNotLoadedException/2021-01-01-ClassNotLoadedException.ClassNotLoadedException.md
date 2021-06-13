---
title: ClassNotLoadedException.ClassNotLoadedException()
permalink: /Java/ClassNotLoadedException/ClassNotLoadedException/
date: 2021-01-11
key: Java.C.ClassNotLoadedException
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassNotLoadedException.constructores valor="ClassNotLoadedException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ClassNotLoadedException(String className)
public ClassNotLoadedException(String className, String message)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Clase Padre
[ClassNotLoadedException](/Java/ClassNotLoadedException/)

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

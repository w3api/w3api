---
title: ClassLoader.setClassAssertionStatus()
permalink: Java/ClassLoader/setClassAssertionStatus
date: 2021-01-11
key: JavaJava.C.ClassLoader
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="setClassAssertionStatus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setClassAssertionStatus(String className, boolean enabled)
~~~

## Parámetros
* **boolean enabled**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enabled" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

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

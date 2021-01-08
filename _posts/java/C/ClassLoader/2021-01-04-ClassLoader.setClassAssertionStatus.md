---
title: ClassLoader.setClassAssertionStatus()
permalink: Java/ClassLoader/setClassAssertionStatus
date: 2021-01-04
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **boolean enabled**,  {% include w3api/param_description.html metodo=_data parametro="boolean enabled" %}

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

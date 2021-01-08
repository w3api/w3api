---
title: ClassLoader.setPackageAssertionStatus()
permalink: Java/ClassLoader/setPackageAssertionStatus
date: 2021-01-04
key: JavaJava.C.ClassLoader
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="setPackageAssertionStatus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPackageAssertionStatus(String packageName, boolean enabled)
~~~

## Parámetros
* **boolean enabled**,  {% include w3api/param_description.html metodo=_data parametro="boolean enabled" %}
* **String packageName**,  {% include w3api/param_description.html metodo=_data parametro="String packageName" %}

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

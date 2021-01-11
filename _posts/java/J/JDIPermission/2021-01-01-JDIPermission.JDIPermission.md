---
title: JDIPermission.JDIPermission()
permalink: Java/JDIPermission/JDIPermission
date: 2021-01-11
key: JavaJava.J.JDIPermission
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JDIPermission.constructores valor="JDIPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JDIPermission(String name)
public JDIPermission(String name, String actions) throws IllegalArgumentException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JDIPermission](/Java/JDIPermission/)

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

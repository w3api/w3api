---
title: RuntimePermission.RuntimePermission()
permalink: /Java/RuntimePermission/RuntimePermission/
date: 2021-01-11
key: Java.R.RuntimePermission
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RuntimePermission.constructores valor="RuntimePermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RuntimePermission(String name)
public RuntimePermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RuntimePermission](/Java/RuntimePermission/)

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

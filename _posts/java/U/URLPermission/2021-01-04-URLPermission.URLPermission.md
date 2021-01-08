---
title: URLPermission.URLPermission()
permalink: Java/URLPermission/URLPermission
date: 2021-01-04
key: JavaJava.U.URLPermission
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLPermission.constructores valor="URLPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public URLPermission(String url)
public URLPermission(String url, String actions)
~~~

## Parámetros
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}
* **String url**,  {% include w3api/param_description.html metodo=_data parametro="String url" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[URLPermission](/Java/URLPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.URLPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

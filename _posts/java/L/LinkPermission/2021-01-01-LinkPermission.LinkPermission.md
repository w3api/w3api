---
title: LinkPermission.LinkPermission()
permalink: /Java/LinkPermission/LinkPermission/
date: 2021-01-11
key: Java.L.LinkPermission
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkPermission.constructores valor="LinkPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LinkPermission(String name)
public LinkPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LinkPermission](/Java/LinkPermission/)

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

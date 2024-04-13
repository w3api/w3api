---
title: AuthPermission.AuthPermission()
permalink: /Java/AuthPermission/AuthPermission/
date: 2021-01-11
key: Java.A.AuthPermission
category: Java
tags: ['java se', 'javax.security.auth', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AuthPermission.constructores valor="AuthPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AuthPermission(String name)
public AuthPermission(String name, String actions)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AuthPermission](/Java/AuthPermission/)

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

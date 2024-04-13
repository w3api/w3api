---
title: UnresolvedPermission.UnresolvedPermission()
permalink: /Java/UnresolvedPermission/UnresolvedPermission/
date: 2021-01-11
key: Java.U.UnresolvedPermission
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UnresolvedPermission.constructores valor="UnresolvedPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public UnresolvedPermission(String type, String name, String actions, Certificate[] certs)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Certificate[] certs**,  {% include w3api/param_description.html metodo=_dato parametro="Certificate[] certs" %}
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Clase Padre
[UnresolvedPermission](/Java/UnresolvedPermission/)

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

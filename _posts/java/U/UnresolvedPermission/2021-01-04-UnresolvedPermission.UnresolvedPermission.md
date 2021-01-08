---
title: UnresolvedPermission.UnresolvedPermission()
permalink: Java/UnresolvedPermission/UnresolvedPermission
date: 2021-01-04
key: JavaJava.U.UnresolvedPermission
category: java
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}
* **Certificate[] certs**,  {% include w3api/param_description.html metodo=_data parametro="Certificate[] certs" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

## Clase Padre
[UnresolvedPermission](/Java/UnresolvedPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UnresolvedPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

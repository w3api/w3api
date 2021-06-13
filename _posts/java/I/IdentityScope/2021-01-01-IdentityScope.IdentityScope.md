---
title: IdentityScope.IdentityScope()
permalink: /Java/IdentityScope/IdentityScope/
date: 2021-01-11
key: Java.I.IdentityScope
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IdentityScope.constructores valor="IdentityScope" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected IdentityScope()
public IdentityScope(String name)
public IdentityScope(String name, IdentityScope scope) throws KeyManagementException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **IdentityScope scope**,  {% include w3api/param_description.html metodo=_dato parametro="IdentityScope scope" %}

## Excepciones
[KeyManagementException](/Java/KeyManagementException/)

## Clase Padre
[IdentityScope](/Java/IdentityScope/)

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

---
title: AccessControlContext.AccessControlContext()
permalink: /Java/AccessControlContext/AccessControlContext/
date: 2021-01-11
key: Java.A.AccessControlContext
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AccessControlContext.constructores valor="AccessControlContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AccessControlContext(AccessControlContext acc, DomainCombiner combiner)
public AccessControlContext(ProtectionDomain[] context)
~~~

## Parámetros
* **AccessControlContext acc**,  {% include w3api/param_description.html metodo=_dato parametro="AccessControlContext acc" %}
* **DomainCombiner combiner**,  {% include w3api/param_description.html metodo=_dato parametro="DomainCombiner combiner" %}
* **ProtectionDomain[] context**,  {% include w3api/param_description.html metodo=_dato parametro="ProtectionDomain[] context" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AccessControlContext](/Java/AccessControlContext/)

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

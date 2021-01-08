---
title: ProtectionDomain.ProtectionDomain()
permalink: Java/ProtectionDomain/ProtectionDomain
date: 2021-01-04
key: JavaJava.P.ProtectionDomain
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProtectionDomain.constructores valor="ProtectionDomain" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProtectionDomain(CodeSource codesource, PermissionCollection permissions)
public ProtectionDomain(CodeSource codesource, PermissionCollection permissions, ClassLoader classloader, Principal[] principals)
~~~

## Parámetros
* **CodeSource codesource**,  {% include w3api/param_description.html metodo=_data parametro="CodeSource codesource" %}
* **ClassLoader classloader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader classloader" %}
* **Principal[] principals**,  {% include w3api/param_description.html metodo=_data parametro="Principal[] principals" %}
* **PermissionCollection permissions**,  {% include w3api/param_description.html metodo=_data parametro="PermissionCollection permissions" %}

## Clase Padre
[ProtectionDomain](/Java/ProtectionDomain/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProtectionDomain.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

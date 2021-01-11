---
title: PolicySpi.engineGetPermissions()
permalink: Java/PolicySpi/engineGetPermissions
date: 2021-01-11
key: JavaJava.P.PolicySpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PolicySpi.metodos valor="engineGetPermissions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected PermissionCollection engineGetPermissions(CodeSource codesource)
protected PermissionCollection engineGetPermissions(ProtectionDomain domain)
~~~

## Parámetros
* **CodeSource codesource**,  {% include w3api/param_description.html metodo=_dato parametro="CodeSource codesource" %}
* **ProtectionDomain domain**,  {% include w3api/param_description.html metodo=_dato parametro="ProtectionDomain domain" %}

## Clase Padre
[PolicySpi](/Java/PolicySpi/)

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

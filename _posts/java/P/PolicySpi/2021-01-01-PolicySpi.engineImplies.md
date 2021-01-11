---
title: PolicySpi.engineImplies()
permalink: Java/PolicySpi/engineImplies
date: 2021-01-11
key: JavaJava.P.PolicySpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PolicySpi.metodos valor="engineImplies" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract boolean engineImplies(ProtectionDomain domain, Permission permission)
~~~

## Parámetros
* **ProtectionDomain domain**,  {% include w3api/param_description.html metodo=_dato parametro="ProtectionDomain domain" %}
* **Permission permission**,  {% include w3api/param_description.html metodo=_dato parametro="Permission permission" %}

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

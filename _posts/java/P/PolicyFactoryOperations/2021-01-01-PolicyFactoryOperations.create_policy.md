---
title: PolicyFactoryOperations.create_policy()
permalink: /Java/PolicyFactoryOperations/create_policy/
date: 2021-01-11
key: Java.P.PolicyFactoryOperations
category: Java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PolicyFactoryOperations.metodos valor="create_policy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Policy create_policy(int type, Any value) throws PolicyError
~~~

## Parámetros
* **Any value**,  {% include w3api/param_description.html metodo=_dato parametro="Any value" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

## Clase Padre
[PolicyFactoryOperations](/Java/PolicyFactoryOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

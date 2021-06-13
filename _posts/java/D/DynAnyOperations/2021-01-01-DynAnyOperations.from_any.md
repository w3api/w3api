---
title: DynAnyOperations.from_any()
permalink: /Java/DynAnyOperations/from_any/
date: 2021-01-11
key: Java.D.DynAnyOperations
category: Java
tags: ['java se', 'org.omg.DynamicAny', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynAnyOperations.metodos valor="from_any" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void from_any(Any value) throws TypeMismatch, InvalidValue
~~~

## Parámetros
* **Any value**,  {% include w3api/param_description.html metodo=_dato parametro="Any value" %}

## Clase Padre
[DynAnyOperations](/Java/DynAnyOperations/)

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

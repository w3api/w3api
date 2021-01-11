---
title: RelationServiceMBean.checkRoleReading()
permalink: Java/RelationServiceMBean/checkRoleReading
date: 2021-01-11
key: JavaJava.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="checkRoleReading" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Integer checkRoleReading(String roleName, String relationTypeName) throws IllegalArgumentException, RelationTypeNotFoundException
~~~

## Parámetros
* **String roleName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleName" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationServiceMBean](/Java/RelationServiceMBean/)

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

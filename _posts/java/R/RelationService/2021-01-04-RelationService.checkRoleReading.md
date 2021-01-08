---
title: RelationService.checkRoleReading()
permalink: Java/RelationService/checkRoleReading
date: 2021-01-04
key: JavaJava.R.RelationService
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="checkRoleReading" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Integer checkRoleReading(String roleName, String relationTypeName) throws IllegalArgumentException, RelationTypeNotFoundException
~~~

## Parámetros
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_data parametro="String relationTypeName" %}
* **String roleName**,  {% include w3api/param_description.html metodo=_data parametro="String roleName" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationService](/Java/RelationService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

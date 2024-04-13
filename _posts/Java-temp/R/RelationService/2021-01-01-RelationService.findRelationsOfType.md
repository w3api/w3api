---
title: RelationService.findRelationsOfType()
permalink: /Java/RelationService/findRelationsOfType/
date: 2021-01-11
key: Java.R.RelationService
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="findRelationsOfType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public List<String> findRelationsOfType(String relationTypeName) throws IllegalArgumentException, RelationTypeNotFoundException
~~~

## Parámetros
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

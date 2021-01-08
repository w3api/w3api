---
title: RelationServiceMBean.hasRelation()
permalink: Java/RelationServiceMBean/hasRelation
date: 2021-01-04
key: JavaJava.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="hasRelation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Boolean hasRelation(String relationId) throws IllegalArgumentException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_data parametro="String relationId" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationServiceMBean](/Java/RelationServiceMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationServiceMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

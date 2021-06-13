---
title: RelationServiceMBean.removeRelationType()
permalink: Java/RelationServiceMBean/removeRelationType
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="removeRelationType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeRelationType(String relationTypeName) throws RelationServiceNotRegisteredException, IllegalArgumentException, RelationTypeNotFoundException
~~~

## Parámetros
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}

## Excepciones
[RelationServiceNotRegisteredException](/Java/RelationServiceNotRegisteredException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/)

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

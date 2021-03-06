---
title: RelationServiceMBean.getRoleInfo()
permalink: /Java/RelationServiceMBean/getRoleInfo/
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="getRoleInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
RoleInfo getRoleInfo(String relationTypeName, String roleInfoName) throws IllegalArgumentException, RelationTypeNotFoundException, RoleInfoNotFoundException
~~~

## Parámetros
* **String roleInfoName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleInfoName" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}

## Excepciones
[RelationTypeNotFoundException](/Java/RelationTypeNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [RoleInfoNotFoundException](/Java/RoleInfoNotFoundException/)

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

---
title: RelationServiceMBean.checkRoleWriting()
permalink: /Java/RelationServiceMBean/checkRoleWriting/
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="checkRoleWriting" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Integer checkRoleWriting(Role role, String relationTypeName, Boolean initFlag) throws IllegalArgumentException, RelationTypeNotFoundException
~~~

## Parámetros
* **Role role**,  {% include w3api/param_description.html metodo=_dato parametro="Role role" %}
* **Boolean initFlag**,  {% include w3api/param_description.html metodo=_dato parametro="Boolean initFlag" %}
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

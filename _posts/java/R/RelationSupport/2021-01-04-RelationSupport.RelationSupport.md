---
title: RelationSupport.RelationSupport()
permalink: Java/RelationSupport/RelationSupport
date: 2021-01-04
key: JavaJava.R.RelationSupport
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationSupport.constructores valor="RelationSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RelationSupport(String relationId, ObjectName relationServiceName, String relationTypeName, RoleList list) throws InvalidRoleValueException, IllegalArgumentException
public RelationSupport(String relationId, ObjectName relationServiceName, MBeanServer relationServiceMBeanServer, String relationTypeName, RoleList list) throws InvalidRoleValueException, IllegalArgumentException
~~~

## Parámetros
* **ObjectName relationServiceName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName relationServiceName" %}
* **String relationId**,  {% include w3api/param_description.html metodo=_data parametro="String relationId" %}
* **MBeanServer relationServiceMBeanServer**,  {% include w3api/param_description.html metodo=_data parametro="MBeanServer relationServiceMBeanServer" %}
* **RoleList list**,  {% include w3api/param_description.html metodo=_data parametro="RoleList list" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_data parametro="String relationTypeName" %}

## Excepciones
[InvalidRoleValueException](/Java/InvalidRoleValueException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RelationSupport](/Java/RelationSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RelationSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

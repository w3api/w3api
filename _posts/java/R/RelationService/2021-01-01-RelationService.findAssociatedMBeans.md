---
title: RelationService.findAssociatedMBeans()
permalink: /Java/RelationService/findAssociatedMBeans/
date: 2021-01-11
key: Java.R.RelationService
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationService.metodos valor="findAssociatedMBeans" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Map<ObjectName,List<String>> findAssociatedMBeans(ObjectName mbeanName, String relationTypeName, String roleName) throws IllegalArgumentException
~~~

## Parámetros
* **String roleName**,  {% include w3api/param_description.html metodo=_dato parametro="String roleName" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relationTypeName" %}
* **ObjectName mbeanName**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName mbeanName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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

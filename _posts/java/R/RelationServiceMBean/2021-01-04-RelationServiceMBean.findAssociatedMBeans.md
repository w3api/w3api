---
title: RelationServiceMBean.findAssociatedMBeans()
permalink: Java/RelationServiceMBean/findAssociatedMBeans
date: 2021-01-04
key: JavaJava.R.RelationServiceMBean
category: java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="findAssociatedMBeans" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Map<ObjectName,List<String>> findAssociatedMBeans(ObjectName mbeanName, String relationTypeName, String roleName) throws IllegalArgumentException
~~~

## Parámetros
* **ObjectName mbeanName**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName mbeanName" %}
* **String relationTypeName**,  {% include w3api/param_description.html metodo=_data parametro="String relationTypeName" %}
* **String roleName**,  {% include w3api/param_description.html metodo=_data parametro="String roleName" %}

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

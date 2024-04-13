---
title: RelationServiceMBean.sendRelationRemovalNotification()
permalink: /Java/RelationServiceMBean/sendRelationRemovalNotification/
date: 2021-01-11
key: Java.R.RelationServiceMBean
category: Java
tags: ['java se', 'javax.management.relation', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelationServiceMBean.metodos valor="sendRelationRemovalNotification" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void sendRelationRemovalNotification(String relationId, List<ObjectName> unregMBeanList) throws IllegalArgumentException, RelationNotFoundException
~~~

## Parámetros
* **String relationId**,  {% include w3api/param_description.html metodo=_dato parametro="String relationId" %}
* **List&lt;ObjectName&gt; unregMBeanList**,  {% include w3api/param_description.html metodo=_dato parametro="List<ObjectName> unregMBeanList" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [RelationNotFoundException](/Java/RelationNotFoundException/)

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

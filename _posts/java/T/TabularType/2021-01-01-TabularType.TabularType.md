---
title: TabularType.TabularType()
permalink: Java/TabularType/TabularType
date: 2021-01-11
key: JavaJava.T.TabularType
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularType.constructores valor="TabularType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TabularType(String typeName, String description, CompositeType rowType, String[] indexNames) throws OpenDataException
~~~

## Parámetros
* **String[] indexNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] indexNames" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}
* **CompositeType rowType**,  {% include w3api/param_description.html metodo=_dato parametro="CompositeType rowType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [OpenDataException](/Java/OpenDataException/)

## Clase Padre
[TabularType](/Java/TabularType/)

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
